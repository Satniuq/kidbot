from language.intents import INTENTS

def resolver(intents, ctx=None):
    if not intents:
        return None

    # regra contextual: continuar história
    if ctx and ctx.memory.mode == "story" and "continuar" in intents:
        return "continuar"

    return max(
        intents,
        key=lambda i: INTENTS[i]["priority"]
    )

