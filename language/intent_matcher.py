from language.intents import INTENTS

def detectar_intencoes(texto_norm):
    encontrados = []

    for intent, data in INTENTS.items():
        for p in data["patterns"]:
            if p in texto_norm:
                encontrados.append(intent)
                break

    return encontrados
