import time
import pymupdf4llm

print("Starting PDF to Markdown conversion for MB20260405.pdf...")
start_time = time.time()

# pymupdf4llm.to_markdown converts the PDF to clean markdown
md_text = pymupdf4llm.to_markdown("MB20260405.pdf")

output_file = "MB20260405.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(md_text)

elapsed = time.time() - start_time
print(f"Successfully converted MB20260405.pdf to {output_file} in {elapsed:.2f} seconds.")
