import random
from response.responses import RESPONSES

def escolher_resposta(intent, response_type):
    banco = RESPONSES.get(intent, {})
    frases = banco.get(response_type)

    if not frases:
        return "Não sei bem o que dizer."

    return random.choice(frases)
