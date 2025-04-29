from pathlib import Path
from typing import List

import pdfplumber

__all__ = ["extract_text_from_pdf"]


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract plain text from a PDF file.

    Parameters
    ----------
    pdf_path : Path
        Absolute or relative path to the PDF file the user uploaded.

    Returns
    -------
    str
        The concatenated text contents of every page in the PDF, with new‑line
        separators preserved where possible. If a page has no text it is
        skipped.
    """

    if not pdf_path.exists() or pdf_path.suffix.lower() != ".pdf":
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    text_chunks: List[str] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text() or ""
            text_chunks.append(extracted)

    # Remove empty strings and join with double new‑lines for readability
    full_text = "\n\n".join(chunk for chunk in text_chunks if chunk.strip())
    return full_text.strip()
