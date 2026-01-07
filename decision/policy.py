# decision/policy.py

def aplicar_politica(ctx):
    """
    Política leve:
    - melhora fallback conforme contexto
    - regista actos (via response_type) para amplitude futura
    """

    # 1) fallback mais inteligente (amplitude sem novos intents)
    if ctx.intent_executed == "fallback":
        if ctx.memory and ctx.memory.mode == "story":
            ctx.response_type = "orientar_story"
        else:
            ctx.response_type = "orientar_meta"

    # 2) registo semântico leve (para evitar repetição / criar progressão)
    if ctx.memory and ctx.intent_executed:
        ctx.memory.register_act(ctx.intent_executed, ctx.response_type)
