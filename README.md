# Script to read scanned PDFs

Using the magic of tesseract to extract text from PDFs which weren't machine written

## Usage

`Usage: python3 app.py <folder with pdf docs>`

## Requirements (Ubuntu 22.04)

- `pdf2image` needs `poppler-utils` installed;

  - `sudo apt install poppler-utils`

- Install Tesseract-ocr

  - `sudo apt install tesseract-ocr`

- And install the external python libraries required
  - `pip install -r requirements.txt`
