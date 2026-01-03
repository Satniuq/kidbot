#handlers.py

import random

# ─────────────────────────────────────────
# FALLBACK
# ─────────────────────────────────────────

def fallback(ctx):
    ctx.state.emocao = "confuso"
    ctx.response_type = "orientar"


# ─────────────────────────────────────────
# MOTOR GENÉRICO DE ESCOLHAS
# ─────────────────────────────────────────

def escolha(ctx):
    choice = ctx.memory.pending_choice
    if not choice:
        ctx.response_type = "confuso"
        return

    intent = ctx.intent_executed
    if intent not in choice["options"]:
        ctx.response_type = "confuso"
        return

    # fecha a escolha
    ctx.memory.pending_choice = None

    # ⚠️ GARANTE que o picker vai procurar em RESPONSES["historia"]
    ctx.intent_executed = choice["domain"]   # aqui SIM, e conscientemente

    # define a resposta concreta (ex: dragao_voar)
    ctx.response_type = choice["options"][intent]

    # só avança narrativa se fizer sentido
    if "next_step" in choice:
        ctx.memory.story_step = choice["next_step"]


# ─────────────────────────────────────────
# WRAPPERS DE OPÇÕES (SEM LÓGICA)
# ─────────────────────────────────────────
def sim(ctx):
    if ctx.memory.pending_choice:
        escolha(ctx)
    else:
        ctx.response_type = "confirmado"


def nao(ctx):
    escolha(ctx)


def voar(ctx):
    escolha(ctx)

def esperar(ctx):
    escolha(ctx)


# ─────────────────────────────────────────
# SAUDAÇÃO
# ─────────────────────────────────────────

def saudacao(ctx):
    ctx.state.emocao = "feliz"

    # resposta inicial
    ctx.response_type = "oferta"

    # cria mini-ciclo de diálogo
    ctx.memory.pending_choice = {
        "domain": "saudacao",
        "options": {
            "historia": "oferecer_historia",
            "ajuda": "oferecer_ajuda"
        }
    }


# ─────────────────────────────────────────
# AJUDA
# ─────────────────────────────────────────
def ajuda(ctx):
    # interrompe qualquer narrativa activa
    if ctx.memory.mode == "story":
        ctx.memory.mode = None
        ctx.memory.story_step = 0
        ctx.memory.pending_choice = None

    ctx.state.emocao = "neutro"
    ctx.response_type = "explicacao"

    ctx.memory.pending_choice = {
        "domain": "ajuda",
        "options": {
            "historia": "oferecer_historia",
            "saudacao": "oferecer_conversa"
        }
    }


# ─────────────────────────────────────────
# NARRATIVA
# ─────────────────────────────────────────

def escolher_historia(memory):
    historias = ["robot", "dragao"]

    if memory.current_story in historias and len(historias) > 1:
        historias = [h for h in historias if h != memory.current_story]

    return random.choice(historias)


def historia(ctx):
    if ctx.memory.mode != "story":
        # limpa qualquer escolha pendente de outros domínios
        ctx.memory.pending_choice = None

        ctx.memory.mode = "story"
        ctx.memory.current_story = escolher_historia(ctx.memory)
        ctx.memory.story_step = 0


    step = ctx.memory.story_step
    ctx.state.emocao = "feliz"

    if step == 0:
        ctx.response_type = "inicio"

    elif step == 1:
        ctx.response_type = "meio"

        # 🔑 CRIA ESCOLHA APENAS COM DADOS
        if ctx.memory.current_story == "dragao" and ctx.memory.pending_choice is None:
            ctx.memory.pending_choice = {
                "domain": "historia",
                "next_step": 2,
                "options": {
                    "voar": "dragao_voar",
                    "esperar": "dragao_esperar"
                }
            }

    elif step == 2:
        ctx.response_type = "climax"

    elif step == 3:
        ctx.response_type = "fim"

        ctx.memory.mode = None
        ctx.memory.story_step = 0

        # 🔑 criar escolha SIM / NÃO
        ctx.memory.pending_choice = {
            "domain": "historia",
            "next_step": 0,
            "options": {
                "sim": "nova_historia",
                "nao": "fim_definitivo"
            }
        }

        return

    ctx.memory.story_step += 1


# ─────────────────────────────────────────
# IDENTIDADE
# ─────────────────────────────────────────

def identidade(ctx):
    ctx.state.emocao = "neutro"

    # primeira vez: apresenta-se e faz pergunta SIM/NÃO
    if ctx.memory.last_intent != "identidade":
        ctx.response_type = "normal"

        ctx.memory.pending_choice = {
            "domain": "identidade",
            "options": {
                "sim": "oferecer_ajuda",
                "nao": "curta"
            }
        }

    # repetição
    else:
        ctx.response_type = "curta"
        ctx.memory.pending_choice = None


# ─────────────────────────────────────────
# OUTROS HANDLERS
# ─────────────────────────────────────────

def despedida(ctx):
    ctx.state.emocao = "neutro"
    ctx.memory.mode = None
    ctx.memory.pending_choice = None
    ctx.response_type = "despedida"
    

def continuar(ctx):
    if ctx.memory.mode == "story":
        ctx.intent_executed = "historia"
        historia(ctx)
    else:
        ctx.response_type = "confuso"


def parar(ctx):
    if ctx.memory.mode == "story":
        ctx.memory.mode = None
        ctx.response_type = "parou"
    else:
        ctx.response_type = "nada_para"

