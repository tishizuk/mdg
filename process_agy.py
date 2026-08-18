# /// script
# dependencies = [
#     "pymupdf",
#     "pymupdf4llm",
#     "ebooklib",
#     "html2text",
# ]
# ///

import os
import sys
import re
import time
import shutil
import unicodedata
from pathlib import Path

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
                cleaned = clean_japanese_text(text)
                md_parts.append(cleaned)
        except Exception as e:
            print(f"  Warning on item {item.get_name()}: {e}")

    full_md = "\n\n---\n\n".join(md_parts).strip()
    if not full_md:
        return False

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
            md_text = clean_japanese_text(md_text)
        except Exception as e:
            print(f"   pymupdf4llmエラー、フォールバック: {e}")
            md_text = extract_vertical_pdf(pdf_path)

    if not md_text or len(md_text) < 10:
        return False

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    return True

def format_vertical_markdown_text(content: str) -> str:
    """縦書き由来のMarkdownテキストの不要な改行・空白を整形し、自然な段落にまとめる"""
    # 1. 特殊文字置換と日本語間空白除去
    content = clean_japanese_text(content)

    # 2. 段落ごとの整形 (Markdown構造を破壊しないように処理)
    blocks = re.split(r'\n{2,}', content)
    formatted_blocks = []

    for block in blocks:
        lines = block.splitlines()
        # コードブロック、表、ヘッダー、リスト項目、引用、画像などはそのまま
        if not lines:
            continue
        first_line = lines[0].strip()
        if (first_line.startswith('```') or first_line.startswith('#') or 
            first_line.startswith('|') or first_line.startswith('---') or
            first_line.startswith('* ') or first_line.startswith('- ') or
            first_line.startswith('> ') or first_line.startswith('![')):
            formatted_blocks.append(block)
            continue

        # 日本語を含む地の文の場合、不要な行内改行を連結
        # 縦書き由来のテキストは1行ごとにぶつ切り改行されている
        joined_lines = []
        cur = ""
        for line in lines:
            l = line.strip()
            if not l:
                continue
            if not cur:
                cur = l
            else:
                # 前の行末が句読点や閉じ括弧などでなく、現在の行の先頭が日本語などの場合、結合
                prev_char = cur[-1]
                curr_char = l[0]
                prev_is_jp = bool(re.search(JP_CHAR_RE, prev_char))
                curr_is_jp = bool(re.search(JP_CHAR_RE, curr_char))
                
                if prev_is_jp and curr_is_jp:
                    cur += l
                elif prev_char in ('、', '，') or curr_char in ('、', '。', '，', '．', '」', '』', '）', '）'):
                    cur += l
                else:
                    cur += " " + l
        if cur:
            formatted_blocks.append(cur)

    result = "\n\n".join(formatted_blocks).strip()
    return result

def clean_and_format_all_md_files(workspace_dir: Path):
    """ワークスペース内のすべての既存Markdownファイルを整形"""
    for md_path in sorted(workspace_dir.glob("*.md")):
        if md_path.name in ("agy.md", "agy_kindle.md", "url.md"):
            continue
        try:
            content = md_path.read_text(encoding="utf-8", errors="ignore")
            cleaned = clean_japanese_text(content)
            if cleaned != content:
                md_path.write_text(cleaned, encoding="utf-8")
                print(f"  [整形完了] {md_path.name}")
        except Exception as e:
            print(f"  [エラー] {md_path.name}: {e}")

def main():
    workspace_dir = Path("/home/tishizuk/Documents/mdg")
    processed_dir = workspace_dir / "processed"
    processed_dir.mkdir(exist_ok=True)

    print("=" * 65)
    print(" agy.md 実行バッチ: PDF/EPUB変換 & 縦書きテキスト整形")
    print("=" * 65)

    # 1. ワークスペース内の未処理 PDF / EPUB ファイルの変換
    print("\n[STEP 1] PDF / EPUB ファイルの検出と変換")
    target_files = []
    for ext in ("*.pdf", "*.epub"):
        for file_path in sorted(workspace_dir.glob(ext)):
            target_files.append(file_path)

    if not target_files:
        print("  対象となる PDF / EPUB ファイルはありません。")
    else:
        print(f"対象ファイル数: {len(target_files)} 件")
        for i, file_path in enumerate(target_files, 1):
            md_path = file_path.with_suffix(".md")
            print(f"\n[{i}/{len(target_files)}] {file_path.name}")

            # processed フォルダに既にあるか確認
            dest_file = processed_dir / file_path.name
            
            # 同名のmdファイルがある場合、変換しないでスキップ
            if md_path.exists():
                print(f"   -> スキップ (同名mdファイルが既に存在): {md_path.name}")
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
                    print(f"   -> テキスト層なし/空ファイルのためmdファイルを作成しませんでした ({elapsed:.1f}秒)")

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
