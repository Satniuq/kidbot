import random

def historia(ctx):
    # se não estamos numa história, começa uma nova
    if ctx.memory.mode != "story":
        ctx.memory.intent_counts["historia"] = 0
        ctx.memory.mode = "story"

        # escolher a história (enredo)
        ctx.memory.current_story = random.choice(["robot", "dragao"])

    count = ctx.memory.intent_counts.get("historia", 0)

    ctx.state.emocao = "feliz"

    if count == 0:
        ctx.response_type = "inicio"

    elif count == 1:
        ctx.response_type = "meio"

    elif count == 2:
        ctx.response_type = "climax"

    elif count == 3:
        ctx.response_type = "fim"
        ctx.memory.mode = None
        ctx.memory.current_story = None

    else:
        ctx.response_type = "fim"


def continuar(ctx):
    if ctx.memory.mode == "story":
        # reutiliza a progressão da história
        ctx.intent = "historia"
        historia(ctx)
    else:
        ctx.response_type = "confuso"

def parar(ctx):
    if ctx.memory.mode == "story":
        ctx.memory.mode = None
        ctx.response_type = "parou"
    else:
        ctx.response_type = "nada_para"


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

def ajuda(ctx):
    ctx.response_type = "explicacao"


def confirmacao(ctx):
    # confirmação depende do modo actual
    if ctx.memory.mode == "story":
        # confirmar = continuar história
        ctx.intent = "historia"
        historia(ctx)
    else:
        ctx.response_type = "confirmado"


def negacao(ctx):
    if ctx.memory.mode == "story":
        ctx.memory.mode = None
        ctx.response_type = "recusou"
    else:
        ctx.response_type = "negou"

