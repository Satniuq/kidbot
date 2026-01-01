#picker.py

import random
from response.responses import RESPONSES

def escolher_resposta(intent, response_type, memory=None):
    banco = RESPONSES.get(intent, {})

    # narrativa com história activa
    if intent == "historia" and memory and memory.current_story:
        banco = banco.get(memory.current_story, {})

    frases = banco.get(response_type)

    if not frases:
        return "Não sei bem o que dizer."

    return random.choice(frases)
