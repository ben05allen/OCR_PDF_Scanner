# Script to read scanned PDFs

Using the magic of tesseract to extract text from PDFs which weren't machine written

## Requirements (Ubuntu 2x.04)

`pdf2image` needs `uv`, `poppler-utils`  and `Tesseract-ocr` installed;

  - `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - `sudo apt install poppler-utils tesseract-ocr`


## Usage
```[bash]
uv run scanner <folder with pdf docs>
```
