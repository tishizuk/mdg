import sys
import time
import pymupdf4llm

pdf_file = sys.argv[1] if len(sys.argv) > 1 else "brother.pdf"
output_file = sys.argv[2] if len(sys.argv) > 2 else pdf_file.rsplit(".", 1)[0] + ".md"

print(f"Starting PDF to Markdown conversion for {pdf_file}...")
start_time = time.time()

md_text = pymupdf4llm.to_markdown(pdf_file)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(md_text)

elapsed = time.time() - start_time
print(f"Successfully converted {pdf_file} to {output_file} in {elapsed:.2f} seconds.")

