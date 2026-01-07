# response/picker.py

import random
from response.responses import RESPONSES


def _expand_template(item):
    """
    item pode ser:
      - str
      - dict {"t": "... {x} ...", "slots": {"x": ["a","b"]}}
    """
    if isinstance(item, str):
        return item

    if isinstance(item, dict) and "t" in item:
        template = item["t"]
        slots = item.get("slots", {})

        # escolhe valores para slots
        chosen = {}
        for k, v in slots.items():
            if isinstance(v, list) and v:
                chosen[k] = random.choice(v)
            else:
                chosen[k] = v

        try:
            return template.format(**chosen)
        except Exception:
            # fallback seguro
            return template

    # fallback se vier algo inesperado
    return str(item)


def escolher_resposta(intent, response_type, memory=None):
    banco = RESPONSES.get(intent, {})

    # narrativa com história activa
    if intent == "historia" and memory and getattr(memory, "current_story", None):
        banco = banco.get(memory.current_story, {})

    frases = banco.get(response_type)

    if not frases:
        return "Não sei bem o que dizer."

    # 1) tenta evitar repetir exactamente a última resposta
    if memory and getattr(memory, "last_response_text", None):
        candidatos = [f for f in frases if _expand_template(f) != memory.last_response_text]
        if candidatos:
            frases = candidatos

    escolhido = random.choice(frases)
    texto = _expand_template(escolhido)

    # 2) guarda última resposta (memória semântica leve)
    if memory is not None:
        memory.last_response_text = texto

    return texto
