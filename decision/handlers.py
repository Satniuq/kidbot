def historia(ctx):
    if ctx.memory.last_intent == "historia":
        ctx.state.emocao = "curioso"
        ctx.response_type = "pergunta"
    else:
        ctx.state.emocao = "feliz"
        ctx.response_type = "longa"


def identidade(ctx):
    if ctx.memory.last_intent == "identidade":
        ctx.state.emocao = "cansado"
        ctx.response_type = "curta"
    else:
        ctx.state.emocao = "neutro"
        ctx.response_type = "normal"


def saudacao(ctx):
    ctx.state.emocao = "feliz"
    ctx.response_type = "curta"
