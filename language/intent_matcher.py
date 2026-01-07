# language/intent_matcher.py

from language.intents import INTENTS


INTENSIFIERS = {
    "mais": "mais",
    "muito": "mais",
    "continua": "normal",
    "depois": "normal",
    "a seguir": "normal"
}


def detectar_intencoes(texto_norm):
    """
    Detecta intenções e devolve uma lista de dicts semânticos.
    Mantém compatibilidade: o nome do intent continua disponível.
    """
    encontrados = []

    texto_norm = texto_norm.strip().lower()

    for intent, data in INTENTS.items():
        for p in data.get("patterns", []):
            if p in texto_norm:
                entrada = {
                    "intent": intent,
                    "canonical": data.get("canonical", intent),
                    "domain": data.get("domain"),
                    "acts": data.get("acts", []),
                    "params": {}
                }

                # ─────────────────────────────────────────
                # Extração semântica simples (Fase 3)
                # ─────────────────────────────────────────

                for palavra, intensidade in INTENSIFIERS.items():
                    if palavra in texto_norm:
                        entrada["params"]["intensidade"] = intensidade
                        break

                encontrados.append(entrada)
                break

    return encontrados
