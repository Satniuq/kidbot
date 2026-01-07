# language/normalizer.py

import unicodedata
import re


def normalizar(texto: str) -> str:
    if not texto:
        return ""

    texto = texto.lower()

    # remove acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )

    # normaliza espaços
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto
