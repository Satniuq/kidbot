#handlers.py

import random

def escolher_historia(memory):
    historias = ["robot", "dragao"]

    # evitar repetir a mesma história seguida
    if memory.current_story in historias and len(historias) > 1:
        historias = [h for h in historias if h != memory.current_story]

    return random.choice(historias)


def historia(ctx):
    if ctx.memory.mode != "story":
        ctx.memory.mode = "story"
        ctx.memory.current_story = escolher_historia(ctx.memory)
        ctx.memory.story_step = 0

    step = ctx.memory.story_step
    ctx.state.emocao = "feliz"

    if step == 0:
        ctx.response_type = "inicio"

    elif step == 1:
        ctx.response_type = "meio"

        # criar escolha narrativa (apenas uma vez)
        if ctx.memory.current_story == "dragao" and ctx.memory.pending_choice is None:
            ctx.memory.pending_choice = {
                "type": "dragao_voar",
                "options": ["voar", "esperar"]
            }

    elif step == 2:
        ctx.response_type = "climax"

    elif step == 3:
        ctx.response_type = "fim"

        # ⚠️ NÃO limpar current_story aqui
        ctx.memory.mode = None
        ctx.memory.story_step = 0
        return

    ctx.memory.story_step += 1

#escolhas narrativas

def voar(ctx):
    if ctx.memory.pending_choice:
        ctx.memory.pending_choice = None

        # 🔑 DOMÍNIO CORRECTO
        ctx.intent_executed = "historia"
        ctx.response_type = "dragao_voar"
        ctx.memory.story_step += 1
    else:
        ctx.response_type = "confuso"


def esperar(ctx):
    if ctx.memory.pending_choice:
        ctx.memory.pending_choice = None

        # 🔑 DOMÍNIO CORRECTO
        ctx.intent_executed = "historia"
        ctx.response_type = "dragao_esperar"
        ctx.memory.story_step += 1
    else:
        ctx.response_type = "confuso"



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

