# pyright: basic

import argparse
from pathlib import Path

from pdf2image import convert_from_path
import pytesseract


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir")
    args = parser.parse_args()

    source_dir = Path(args.source_dir)
    pdf_docs = [f for f in Path(source_dir).glob("*.pdf")]

    for pdf_doc in pdf_docs:
        doc = convert_from_path(pdf_doc, 500)  # pyright: ignore

        print(f"Scanning doc: {pdf_doc}")
        for page, scan in enumerate(doc):
            text = pytesseract.image_to_string(scan)
            print(f"Page {page}:\n{text}")
