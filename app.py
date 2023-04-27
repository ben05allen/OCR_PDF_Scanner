import sys
from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

if len(sys.argv) != 2:
    print('Usage: python3 app.py <folder>')
    sys.exit(1)

source_dir = Path(sys.argv[1])
pdf_docs = [f for f in Path(source_dir).glob('*.pdf')]

for pdf_doc in pdf_docs:
    doc = convert_from_path(pdf_doc, 500)

    print(f'Scanning doc: {pdf_doc}')
    for page, scan in enumerate(doc):
        text = pytesseract.image_to_string(scan)
        print(f'Page {page}:\n{text}')
