import os
import sys
import time
import shutil
from pathlib import Path

def convert_epub_to_md(epub_path: Path, md_path: Path):
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
    
    # Try reading by spine order first
    items = []
    item_ids = [item[0] for item in book.spine]
    for item_id in item_ids:
        item = book.get_item_with_id(item_id)
        if item and item.get_type() == ebooklib.ITEM_DOCUMENT:
            items.append(item)
            
    # Fallback if spine is empty or incomplete
    if not items:
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

    md_parts = []
    for item in items:
        try:
            content = item.get_content().decode("utf-8", errors="ignore")
            text = h.handle(content).strip()
            if text:
                md_parts.append(text)
        except Exception as e:
            print(f"  Warning on item {item.get_name()}: {e}")

    full_md = "\n\n---\n\n".join(md_parts)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_md)

def convert_pdf_to_md(pdf_path: Path, md_path: Path):
    import pymupdf4llm

    md_text = pymupdf4llm.to_markdown(str(pdf_path))
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)

def main():
    workspace_dir = Path("/home/tishizuk/Documents/mdg")
    processed_dir = workspace_dir / "processed"
    processed_dir.mkdir(exist_ok=True)
    
    # Find all pdf and epub files in the workspace root
    target_files = []
    for ext in ("*.pdf", "*.epub"):
        for file_path in sorted(workspace_dir.glob(ext)):
            md_path = file_path.with_suffix(".md")
            if not md_path.exists():
                target_files.append((file_path, md_path))

    if not target_files:
        print("未変換のPDF/EPUBファイルはありません。")
        return

    print(f"未変換ファイル数: {len(target_files)} 件")
    for file_path, md_path in target_files:
        print(f" - {file_path.name} -> {md_path.name}")
    print("=" * 60)

    for i, (file_path, md_path) in enumerate(target_files, 1):
        print(f"[{i}/{len(target_files)}] 変換中: {file_path.name} ...", flush=True)
        start_time = time.time()
        try:
            if file_path.suffix.lower() == ".epub":
                convert_epub_to_md(file_path, md_path)
            elif file_path.suffix.lower() == ".pdf":
                convert_pdf_to_md(file_path, md_path)
            
            elapsed = time.time() - start_time
            size_mb = md_path.stat().st_size / (1024 * 1024)
            print(f"  -> 変換完了 ({elapsed:.1f}秒, {size_mb:.2f} MB)", flush=True)

            # Move processed original file to processed/ folder
            dest_file = processed_dir / file_path.name
            shutil.move(str(file_path), str(dest_file))
            print(f"  -> processed/ へ移動しました", flush=True)
        except Exception as e:
            print(f"  -> エラー発生: {e}", flush=True)

    print("=" * 60)
    print("すべての処理が完了しました。")

if __name__ == "__main__":
    main()
