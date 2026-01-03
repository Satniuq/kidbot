#conflict_resolver.py

from language.intents import INTENTS

GLOBAL_INTENTS = {"ajuda", "identidade", "parar"}

def resolver(intents, ctx=None):
    # 🟢 intents globais furam qualquer escolha pendente
    if ctx and ctx.memory.pending_choice:
        for intent in intents:
            if intent in GLOBAL_INTENTS:
                return intent

        # se não for global, tenta resolver a escolha
        for opt in ctx.memory.pending_choice["options"]:
            if opt in intents:
                return opt

    if not intents:
        return None

    # regra contextual: continuar história
    if ctx and ctx.memory.mode == "story" and "continuar" in intents:
        return "continuar"

    return max(
        intents,
        key=lambda i: INTENTS[i]["priority"]
    )
