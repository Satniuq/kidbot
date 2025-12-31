from language.intents import INTENTS

def detectar_intencoes(texto_norm):
    encontrados = []

    texto_norm = texto_norm.strip().lower()

    for intent, data in INTENTS.items():
        for p in data["patterns"]:
            if p in texto_norm:
                encontrados.append(intent)
                break

    return encontrados
