# /// script
# dependencies = [
#     "pymupdf",
#     "pymupdf4llm",
#     "ebooklib",
#     "html2text",
#     "google-genai",
#     "python-dotenv",
#     "pillow",
# ]
# ///

import os
import sys
import re
import time
import shutil
import zipfile
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- 環境変数の読み込み (GEMINI_API_KEY from ~/.env) ---
def load_env():
    env_path = Path.home() / ".env"
    if not env_path.exists():
        return {}
    with open(env_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            k = k.strip()
            v = v.strip().strip("\"'")
            os.environ[k] = v

load_env()

# --- 文字マッピング辞書 ---
CHAR_MAP = {
    # Control Pictures / Kindle縦書きフォントの小書き・長音記号
    '\u2417': 'ー', '\u241a': '〜',
    '\u2432': 'っ', '\u2433': 'ぁ', '\u2434': 'ぃ', '\u2435': 'ぇ', '\u2436': 'ぉ',
    '\u2437': 'っ', '\u2438': 'ゃ', '\u2439': 'ゅ', '\u243a': 'ょ', '\u243b': 'ゎ',
    '\u243c': 'ァ', '\u243d': 'ィ', '\u243e': 'ゥ', '\u243f': 'ェ',
    '\u2440': 'ォ', '\u2441': 'ッ', '\u2442': 'ャ', '\u2443': 'ュ', '\u2444': 'ョ',
    '\u2446': 'ヵ', '\u2447': 'ヶ',
    # 岩波文庫などの外字
    '\u1f00': 'ャ', '\u1f01': 'ュ', '\u1f02': 'ョ', '\u1ed5': 'ー',
    # 縦書き用約物 (Presentation Forms for Vertical)
    '﹁': '「', '﹂': '」', '﹃': '『', '﹄': '』',
    '︑': '、', '︒': '。', '︙': '…', '︱': '―', '︲': '―', '︴': '〜',
    '︵': '（', '︶': '）', '︷': '｛', '︸': '｝', '︹': '〔', '︺': '〕',
    '︻': '【', '︼': '】', '︽': '《', '︾': '》', '︿': '〈', '﹀': '〉',
    '﹇': '〔', '﹈': '〕', '︕': '！', '︖': '？', '︓': '：', '︔': '；',
    # CJK Extension A 領域の縦書き外字 (青空文庫/Kindle等)
    '䣍': '、', '䣎': '。',
    '䣏': '「', '䣐': '」', '䣑': '「', '䣒': '」', '䣓': '「', '䣔': '」',
    '䣕': '『', '䣖': '』', '䣣': '「', '䣥': '」',
    '䣧': 'ぁ', '䣪': 'ぇ', '䣫': 'ぉ', '䣬': 'っ',
    '䣭': 'ゃ', '䣮': 'ゅ', '䣯': 'ょ',
    '䣴': 'ァ', '䣵': 'ィ', '䣶': 'ゥ', '䣷': 'ェ', '䣸': 'ォ', '䣹': 'ッ',
    '䣺': 'ャ', '䣻': 'ュ', '䣼': 'ョ', '䣾': 'ヵ', '䣿': 'ヶ', '䤀': 'ー',
    '䥹': '（', '䥺': '）', '䥽': '：', '䥿': 'た',
}

JP_CHAR_RE = r'[\u3000-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]'

def clean_japanese_text(text: str) -> str:
    """特殊文字のマッピングとNFKC正規化、および日本語間の不要な空白除去"""
    for k, v in CHAR_MAP.items():
        text = text.replace(k, v)
    text = unicodedata.normalize('NFKC', text)
    # 日本語文字間のスペース除去 (複数回適用)
    text = re.sub(f'({JP_CHAR_RE})[ \t]+({JP_CHAR_RE})', r'\1\2', text)
    text = re.sub(f'({JP_CHAR_RE})[ \t]+({JP_CHAR_RE})', r'\1\2', text)
    return text

def format_vertical_markdown_text(content: str) -> str:
    """縦書き由来のMarkdownテキストの不要な改行・空白を整形し、自然な段落にまとめる"""
    # 1. コードブロックを一時退避
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"\x00CODEBLOCK_{len(code_blocks)-1}\x00"

    content = re.sub(r'```[\s\S]*?```', save_code_block, content)

    # 2. 特殊文字置換と日本語間空白除去
    content = clean_japanese_text(content)

    # 3. 段落ごとの整形
    blocks = re.split(r'\n{2,}', content)
    formatted_blocks = []

    for block in blocks:
        lines = block.splitlines()
        if not lines:
            continue

        # ヘッダー、表、区切り線、コードブロックプレースホルダー等のチェック
        first_line = lines[0].strip()
        if (first_line.startswith('\x00CODEBLOCK_') or 
            first_line.startswith('#') or 
            first_line.startswith('|') or 
            first_line.startswith('---') or
            first_line.startswith('***') or
            first_line.startswith('___') or
            first_line.startswith('* ') or 
            first_line.startswith('- ') or 
            first_line.startswith('+ ') or
            re.match(r'^\d+\.\s', first_line) or
            first_line.startswith('> ') or 
            first_line.startswith('![')):
            formatted_blocks.append(block)
            continue

        # 地の文の不要な行内改行を結合
        cur = ""
        for line in lines:
            l = line.strip()
            if not l:
                continue
            if not cur:
                cur = l
            else:
                prev_char = cur[-1]
                curr_char = l[0]
                prev_is_jp = bool(re.search(JP_CHAR_RE, prev_char))
                curr_is_jp = bool(re.search(JP_CHAR_RE, curr_char))

                if prev_is_jp and curr_is_jp:
                    cur += l
                elif prev_char in ('、', '，', '（', '「', '『') or curr_char in ('、', '。', '，', '．', '」', '』', '）', '！', '？'):
                    cur += l
                elif prev_is_jp or curr_is_jp:
                    cur += l
                else:
                    cur += " " + l
        if cur:
            formatted_blocks.append(cur)

    result = "\n\n".join(formatted_blocks).strip()

    # 4. コードブロック復元
    for i, cb in enumerate(code_blocks):
        result = result.replace(f"\x00CODEBLOCK_{i}\x00", cb)

    # 5. 不要な空テーブル行・孤立した区切り線の除去
    result = clean_tables_in_text(result)

    # 6. 連続改行の正規化
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result

def is_empty_table_row(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    inner = stripped
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    cells = inner.split("|")
    return all(c.strip() == "" for c in cells)

def is_table_separator(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    inner = stripped
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    cells = inner.split("|")
    return bool(cells) and all(bool(re.match(r'^\s*:?-+:?\s*$', c)) for c in cells if c.strip())

def clean_tables_in_text(text: str) -> str:
    lines = text.splitlines()
    filtered_lines = [l for l in lines if not is_empty_table_row(l)]
    
    result_lines = []
    i = 0
    while i < len(filtered_lines):
        line = filtered_lines[i]
        if is_table_separator(line):
            if result_lines and result_lines[-1].strip().startswith("|") and not is_table_separator(result_lines[-1]):
                result_lines.append(line)
            else:
                if i + 1 < len(filtered_lines) and filtered_lines[i+1].strip().startswith("|") and not is_table_separator(filtered_lines[i+1]):
                    next_row = filtered_lines[i+1]
                    result_lines.append(next_row)
                    result_lines.append(line)
                    i += 2
                    continue
                else:
                    i += 1
                    continue
        else:
            result_lines.append(line)
        i += 1
        
    return "\n".join(result_lines)

# --- 固定レイアウト判定 & Gemini API OCR ---

def is_fixed_layout_epub(epub_path: Path) -> bool:
    """EPUBが固定レイアウト（プリント・レプリカ含む画像書式）かどうか判定"""
    if "プリント・レプリカ" in epub_path.name or "print replica" in epub_path.name.lower():
        return True
    try:
        with zipfile.ZipFile(epub_path, 'r') as z:
            names = z.namelist()
            xhtml_files = [n for n in names if n.endswith('.xhtml') or n.endswith('.html')]
            if not xhtml_files:
                return True
            # 数ファイルをサンプリングして画像のみのラッパーか確認
            sample = xhtml_files[:min(10, len(xhtml_files))]
            text_lengths = []
            for s in sample:
                content = z.read(s).decode('utf-8', errors='ignore')
                raw_text = re.sub(r'<[^>]+>', '', content).strip()
                text_lengths.append(len(raw_text))
            if max(text_lengths, default=0) < 30:
                return True
    except Exception:
        pass
    return False

def convert_fixed_layout_images_with_gemini(image_paths: list[Path], output_md: Path, book_title: str) -> bool:
    """Gemini API (3.7 Flash) を用いて画像群を高精度Markdownに変換して保存"""
    from google import genai
    from google.genai import types

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("   [Gemini API エラー] GEMINI_API_KEY が ~/.env に見つかりません。")
        return False

    client = genai.Client(api_key=api_key)

    cache_dir = Path("/home/tishizuk/Documents/mdg") / f"scratch_cache_{re.sub(r'[^a-zA-Z0-9]', '_', book_title[:30])}"
    cache_dir.mkdir(parents=True, exist_ok=True)

    total_pages = len(image_paths)
    print(f"   [Gemini VLM 変換] 総ページ数: {total_pages} ページを並列処理します...")

    prompt_text = (
        "あなたは技術書や専門書の文字起こしを行う最高精度のエキスパートです。画像の内容を忠実にMarkdown形式で書き起こしてください。\n"
        "【重要なルール】\n"
        "1. プログラムコードやコマンド、REPL・ターミナル出力は、必ず適切な言語タグ（```zsh, ```bash, ```python など）を付けたコードブロックで正確に記述してください。\n"
        "   - 本文画像のコードに行番号（「1 | 」「2 | 」など）が付いている場合、行番号は除去して純粋な実行可能コードのみを記載してください。\n"
        "2. 数式がある場合は必ずLaTeX形式（インラインは $...$ 、独立行は $$...$$）で正確に記述してください。\n"
        "3. 章・節・項の見出しは適切なMarkdown見出し（#、##、###、####）に変換してください。\n"
        "4. 箇条書き、番号付きリスト、表（テーブル）もMarkdown記法で忠実に再現してください。\n"
        "5. ページ上部や下部の単独のページ番号や柱（章タイトルのみのヘッダー・フッター）は省略してください。\n"
        "6. RAG（検索拡張生成）用のナレッジベースとして利用されるため、文脈が分かりやすく、ノイズの少ない綺麗なMarkdownにしてください。\n"
        "7. 余計な挨拶や説明は一切出力せず、書き起こしたMarkdown本文のみを出力してください。"
    )

    def process_page(idx, img_path):
        cache_file = cache_dir / f"page_{idx:04d}.txt"
        if cache_file.exists():
            return idx, cache_file.read_text(encoding="utf-8"), True

        img_bytes = img_path.read_bytes()
        suffix = img_path.suffix.lower()
        mime_type = "image/png" if suffix == ".png" else "image/jpeg"

        max_retries = 5
        for attempt in range(max_retries):
            try:
                resp = client.models.generate_content(
                    model="gemini-3.7-flash",
                    contents=[
                        types.Part.from_bytes(data=img_bytes, mime_type=mime_type),
                        prompt_text
                    ]
                )
                text = resp.text.strip() if resp.text else ""
                cache_file.write_text(text, encoding="utf-8")
                return idx, text, False
            except Exception as e:
                wait_sec = (2 ** attempt) * 2
                print(f"     [ページ {idx+1}/{total_pages}] 再試行 {attempt+1}/{max_retries} ({e}). {wait_sec}秒待機...")
                time.sleep(wait_sec)

        error_text = f"<!-- エラー: ページ {idx+1} の処理に失敗しました -->"
        cache_file.write_text(error_text, encoding="utf-8")
        return idx, error_text, False

    results = {}
    max_workers = 10
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_page, idx, img_path): idx for idx, img_path in enumerate(image_paths)}
        completed_count = 0
        for future in as_completed(futures):
            idx, text, from_cache = future.result()
            results[idx] = text
            completed_count += 1
            if completed_count % 20 == 0 or completed_count == total_pages:
                status_str = "キャッシュ利用" if from_cache else "API処理"
                print(f"     進行状況: [{completed_count}/{total_pages}] ({status_str})")

    elapsed = time.time() - start_time
    print(f"   [Gemini VLM 完了] {total_pages} ページの処理が完了しました ({elapsed:.1f}秒)")

    # 結合 & 整形
    all_pages = []
    for i in range(total_pages):
        p_text = results.get(i, "").strip()
        if p_text.startswith("```markdown") and p_text.endswith("```"):
            p_text = p_text[len("```markdown"): -3].strip()
        if p_text:
            all_pages.append(p_text)

    full_md = "\n\n---\n\n".join(all_pages).strip()
    formatted_md = format_vertical_markdown_text(full_md)
    output_md.write_text(formatted_md, encoding="utf-8")
    return True

def convert_fixed_layout_epub_with_gemini(epub_path: Path, md_path: Path) -> bool:
    """固定レイアウトEPUB内の全ページ画像を抽出してGemini APIで変換"""
    import pymupdf
    print(f"   [固定レイアウトEPUB検出] 画像ページを抽出中...")
    extract_dir = Path("/home/tishizuk/Documents/mdg") / f"scratch_pages_{re.sub(r'[^a-zA-Z0-9]', '_', epub_path.stem[:30])}"
    extract_dir.mkdir(parents=True, exist_ok=True)

    image_paths = []
    with zipfile.ZipFile(epub_path, 'r') as z:
        names = z.namelist()
        opf_files = [n for n in names if n.endswith('.opf')]
        if opf_files:
            opf_name = opf_files[0]
            opf_dir = str(Path(opf_name).parent)
            if opf_dir == ".":
                opf_dir = ""
            
            opf_content = z.read(opf_name)
            root = ET.fromstring(opf_content)
            
            manifest = {}
            for item in root.iter():
                if item.tag.endswith('item') and 'id' in item.attrib:
                    manifest[item.attrib['id']] = item.attrib.get('href')
                    
            spine_ids = []
            for itemref in root.iter():
                if itemref.tag.endswith('itemref') and 'idref' in itemref.attrib:
                    spine_ids.append(itemref.attrib['idref'])
                    
            for idx, idref in enumerate(spine_ids):
                href = manifest.get(idref)
                if not href:
                    continue
                full_href = f"{opf_dir}/{href}".lstrip("/") if opf_dir else href
                if full_href in names:
                    doc_content = z.read(full_href).decode('utf-8', errors='ignore')
                    m = re.search(r'(?:src|xlink:href)=[\"\']([^\"\']+)[\"\']', doc_content, re.I)
                    if m:
                        target_rel = m.group(1)
                        doc_parent = str(Path(full_href).parent)
                        target_full = f"{doc_parent}/{target_rel}".lstrip("/") if doc_parent != "." else target_rel
                        target_full = str(Path(target_full)).replace("\\", "/")
                        if target_full in names:
                            img_out = extract_dir / f"page_{idx:04d}.png"
                            if not img_out.exists():
                                data = z.read(target_full)
                                if target_full.lower().endswith('.pdf'):
                                    doc = pymupdf.open(stream=data, filetype="pdf")
                                    pix = doc[0].get_pixmap(dpi=150)
                                    pix.save(str(img_out))
                                    doc.close()
                                else:
                                    img_out.write_bytes(data)
                            image_paths.append(img_out)

    if not image_paths:
        # フォールバック: zip内のすべての画像/PDFファイルを名前順で抽出
        with zipfile.ZipFile(epub_path, 'r') as z:
            all_targets = [n for n in sorted(z.namelist()) if re.search(r'\.(jpe?g|png|pdf)$', n, re.I) and not n.startswith('__')]
            for idx, target_name in enumerate(all_targets):
                img_out = extract_dir / f"page_{idx:04d}.png"
                if not img_out.exists():
                    data = z.read(target_name)
                    if target_name.lower().endswith('.pdf'):
                        doc = pymupdf.open(stream=data, filetype="pdf")
                        pix = doc[0].get_pixmap(dpi=150)
                        pix.save(str(img_out))
                        doc.close()
                    else:
                        img_out.write_bytes(data)
                image_paths.append(img_out)

    if not image_paths:
        print("   -> 有効なページ画像が見つかりませんでした。")
        return False

    return convert_fixed_layout_images_with_gemini(image_paths, md_path, epub_path.stem)

def convert_fixed_layout_pdf_with_gemini(pdf_path: Path, md_path: Path) -> bool:
    """テキスト層のないPDFを画像レンダリングしてGemini APIで変換"""
    import pymupdf
    print(f"   [画像PDF検出] PDFページを画像にレンダリング中...")
    extract_dir = Path("/home/tishizuk/Documents/mdg") / f"scratch_pages_{re.sub(r'[^a-zA-Z0-9]', '_', pdf_path.stem[:30])}"
    extract_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(str(pdf_path))
    image_paths = []
    for idx, page in enumerate(doc):
        img_out = extract_dir / f"page_{idx:04d}.png"
        if not img_out.exists():
            pix = page.get_pixmap(dpi=150)
            pix.save(str(img_out))
        image_paths.append(img_out)
    doc.close()

    return convert_fixed_layout_images_with_gemini(image_paths, md_path, pdf_path.stem)

# --- 通常のPDF/EPUB抽出処理 ---

def is_vertical_pdf(doc) -> bool:
    """PDFが縦書きかどうか判定する"""
    vert_count = 0
    total_checked = 0
    
    num_pages = len(doc)
    pages_to_check = [0, num_pages // 4, num_pages // 2, 3 * num_pages // 4, min(num_pages - 1, 10)]
    pages_to_check = sorted(list(set(p for p in pages_to_check if p < num_pages)))

    for pno in pages_to_check:
        page = doc[pno]
        blocks = page.get_text('blocks')
        for b in blocks:
            if b[6] != 0:
                continue
            text = b[4].strip()
            if not text or len(text) < 3:
                continue
            total_checked += 1
            w = b[2] - b[0]
            h = b[3] - b[1]
            if h > w * 1.5:
                vert_count += 1
            elif any(c in text for c in ['﹁', '﹂', '︑', '︒', '\u2437', '\u2417', '\u2442', '䣎', '䣍', '䣬', '䣓']):
                vert_count += 1

    if total_checked == 0:
        return False
    return (vert_count / total_checked) > 0.3

def extract_vertical_pdf(pdf_path: Path) -> str:
    """縦書きPDFから自然な横書きMarkdownテキストを抽出する"""
    import pymupdf
    doc = pymupdf.open(str(pdf_path))
    pages_text = []

    for page in doc:
        p_height = page.rect.height
        blocks = page.get_text('blocks')
        
        text_blocks = []
        for b in blocks:
            if b[6] != 0:
                continue
            t = b[4].strip()
            if not t:
                continue
            y0, y1 = b[1], b[3]
            # ヘッダー/フッター除外
            if (y0 < 30 or y1 > p_height - 30) and len(t) <= 6:
                continue
            text_blocks.append(b)

        if not text_blocks:
            continue

        # 縦書きは右から左へ並ぶ
        text_blocks.sort(key=lambda b: -b[0])

        col_texts = []
        for b in text_blocks:
            raw = b[4]
            lines = [l.strip() for l in raw.splitlines() if l.strip()]
            joined = ''.join(lines)
            cleaned = clean_japanese_text(joined)
            if cleaned:
                col_texts.append(cleaned)

        if not col_texts:
            continue

        page_paras = []
        cur_para = ""

        for col in col_texts:
            if not cur_para:
                cur_para = col
            else:
                ends_with_punct = cur_para[-1] in ('。', '！', '？', '…', '」', '』', '”', '；')
                starts_with_open = col[0] in ('「', '『', '（', '【', '“', '〔', '第', '●', '#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十')
                is_short_heading = len(col) < 15 and (col.startswith('第') or col.startswith('章') or col.startswith('目次'))

                if ends_with_punct or (starts_with_open and cur_para.endswith('。')) or is_short_heading:
                    page_paras.append(cur_para)
                    cur_para = col
                else:
                    cur_para += col

        if cur_para:
            page_paras.append(cur_para)

        page_str = "\n\n".join(page_paras).strip()
        if page_str:
            pages_text.append(page_str)

    return "\n\n".join(pages_text).strip()

def convert_epub_to_md(epub_path: Path, md_path: Path) -> bool:
    # 1. 固定レイアウト・プリントレプリカ判定
    if is_fixed_layout_epub(epub_path):
        return convert_fixed_layout_epub_with_gemini(epub_path, md_path)

    # 2. リフロー型EPUBのテキスト抽出
    import ebooklib
    from ebooklib import epub
    import html2text
    import warnings
    warnings.filterwarnings("ignore")

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0

    book = epub.read_epub(str(epub_path))
    
    items = []
    item_ids = [item[0] for item in book.spine]
    for item_id in item_ids:
        item = book.get_item_with_id(item_id)
        if item and item.get_type() == ebooklib.ITEM_DOCUMENT:
            items.append(item)
            
    if not items:
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    md_parts = []
    for item in items:
        try:
            content = item.get_content().decode("utf-8", errors="ignore")
            text = h.handle(content).strip()
            if text:
                formatted = format_vertical_markdown_text(text)
                md_parts.append(formatted)
        except Exception as e:
            print(f"  Warning on item {item.get_name()}: {e}")

    full_md = "\n\n---\n\n".join(md_parts).strip()
    if not full_md or len(full_md) < 50:
        # テキストがほとんど抽出できなかった場合は固定レイアウトとしてGeminiにフォールバック
        return convert_fixed_layout_epub_with_gemini(epub_path, md_path)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_md)
    return True

def convert_pdf_to_md(pdf_path: Path, md_path: Path) -> bool:
    import pymupdf
    import pymupdf4llm

    doc = pymupdf.open(str(pdf_path))
    if len(doc) == 0:
        return False

    is_vert = is_vertical_pdf(doc)
    doc.close()

    if is_vert:
        print(f"   [縦書き検出] 縦書き整形抽出を実行中...")
        md_text = extract_vertical_pdf(pdf_path)
    else:
        print(f"   [横書き検出] pymupdf4llm を実行中...")
        try:
            md_text = pymupdf4llm.to_markdown(str(pdf_path)).strip()
            md_text = format_vertical_markdown_text(md_text)
        except Exception as e:
            print(f"   pymupdf4llmエラー、フォールバック: {e}")
            md_text = extract_vertical_pdf(pdf_path)

    if not md_text or len(md_text) < 50:
        print("   -> テキスト層が極小/なしのため Gemini VLM OCR にフォールバックします...")
        return convert_fixed_layout_pdf_with_gemini(pdf_path, md_path)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    return True

def clean_and_format_all_md_files(workspace_dir: Path):
    """ワークスペース内のすべての既存Markdownファイルを整形"""
    updated_count = 0
    total_count = 0
    for md_path in sorted(workspace_dir.glob("*.md")):
        if md_path.name in ("agy.md", "agy_kindle.md", "url.md"):
            continue
        total_count += 1
        try:
            content = md_path.read_text(encoding="utf-8", errors="ignore")
            cleaned = format_vertical_markdown_text(content)
            if cleaned != content:
                md_path.write_text(cleaned, encoding="utf-8")
                updated_count += 1
                print(f"  [整形完了] {md_path.name}")
        except Exception as e:
            print(f"  [エラー] {md_path.name}: {e}")
    print(f"  既存Markdownファイル整形完了: {updated_count}/{total_count} ファイルを更新しました")

def main():
    workspace_dir = Path("/home/tishizuk/Documents/mdg")
    processed_dir = workspace_dir / "processed"
    processed_dir.mkdir(exist_ok=True)

    print("=" * 65)
    print(" agy.md 実行バッチ: PDF/EPUB変換 & 縦書きテキスト整形")
    print("=" * 65)

    # 1. ワークスペース内の未処理 PDF / EPUB ファイルの検出と変換
    print("\n[STEP 1] PDF / EPUB ファイルの検出と変換")
    target_files = []
    for ext in ("*.pdf", "*.epub"):
        for file_path in sorted(workspace_dir.glob(ext)):
            if (processed_dir / file_path.name).exists():
                print(f"   -> 既に processed/ に存在するため移動: {file_path.name}")
                file_path.unlink()
                continue
            target_files.append(file_path)

    if not target_files:
        print("  対象となる未処理の PDF / EPUB ファイルはありません。")
    else:
        print(f"対象ファイル数: {len(target_files)} 件")
        for i, file_path in enumerate(target_files, 1):
            md_path = file_path.with_suffix(".md")
            print(f"\n[{i}/{len(target_files)}] {file_path.name}")

            # 同名のmdファイルがある場合、変換しないでスキップ
            if md_path.exists():
                print(f"   -> スキップ (同名mdファイルが既に存在): {md_path.name}")
                dest_file = processed_dir / file_path.name
                shutil.move(str(file_path), str(dest_file))
                print(f"   -> processed/ へ移動しました")
                continue

            print(f"   -> 変換中...", flush=True)
            start_time = time.time()
            try:
                success = False
                if file_path.suffix.lower() == ".epub":
                    success = convert_epub_to_md(file_path, md_path)
                elif file_path.suffix.lower() == ".pdf":
                    success = convert_pdf_to_md(file_path, md_path)

                elapsed = time.time() - start_time
                if success:
                    size_mb = md_path.stat().st_size / (1024 * 1024)
                    print(f"   -> 変換完了 ({elapsed:.1f}秒, {size_mb:.2f} MB)")
                else:
                    print(f"   -> 変換できませんでした ({elapsed:.1f}秒)")

                dest_file = processed_dir / file_path.name
                shutil.move(str(file_path), str(dest_file))
                print(f"   -> processed/ へ移動しました")
            except Exception as e:
                print(f"   -> エラー発生: {e}")

    # 2. 既存Markdownファイルのテキストクリーンアップ & 縦書き整形
    print("\n[STEP 2] 既存 Markdown ファイルの縦書き由来テキスト整形 & クリーンアップ")
    clean_and_format_all_md_files(workspace_dir)

    print("\n" + "=" * 65)
    print(" agy.md のすべての処理が正常に完了しました！")
    print("=" * 65)

if __name__ == "__main__":
    main()
