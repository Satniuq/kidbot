from language.intents import INTENTS

def resolver(intents):
    if not intents:
        return None

    return max(
        intents,
        key=lambda i: INTENTS[i]["priority"]
    )
