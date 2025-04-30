# app/utils/extract_text.py

import io
from typing import Union
from werkzeug.datastructures import FileStorage

import pdfplumber
import docx


def extract_text(file: FileStorage) -> str:
    """
    Given a FileStorage (PDF, DOCX or TXT), returns its full text content.
    """
    filename = file.filename.lower()

    # PDF → use pdfplumber
    if filename.endswith(".pdf"):
        return _extract_pdf(file)

    # DOCX → use python-docx
    elif filename.endswith(".docx"):
        return _extract_docx(file)

    # Plain text → decode directly
    elif filename.endswith(".txt"):
        content = file.read()
        try:
            return content.decode("utf-8", errors="ignore")
        finally:
            file.stream.seek(0)

    else:
        raise ValueError(f"Unsupported file type: {filename}")


def _extract_pdf(file: FileStorage) -> str:
    text_chunks = []
    # wrap stream in a BytesIO
    with pdfplumber.open(io.BytesIO(file.read())) as pdf:
        for page in pdf.pages:
            text_chunks.append(page.extract_text() or "")
    # reset for any later reads
    file.stream.seek(0)
    return "\n".join(text_chunks)


def _extract_docx(file: FileStorage) -> str:
    text_chunks = []
    # python-docx expects a filename or a file-like, so wrap stream
    document = docx.Document(io.BytesIO(file.read()))
    for para in document.paragraphs:
        text_chunks.append(para.text)
    file.stream.seek(0)
    return "\n".join(text_chunks)