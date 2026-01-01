#conflict_resolver.py

from language.intents import INTENTS

def resolver(intents, ctx=None):
    # 🟢 prioridade máxima: escolha pendente
    if ctx and ctx.memory.pending_choice:
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
