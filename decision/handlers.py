#handlers.py

import random

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

    ctx.memory.pending_choice = None
    ctx.intent_executed = choice["domain"]
    ctx.response_type = choice["options"][intent]


    # 🔑 CASO ESPECIAL: nova história
    if ctx.response_type == "nova_historia":
        ctx.memory.mode = "story"
        ctx.memory.current_story = None
        ctx.memory.story_step = 0

        # falar a frase "Então vamos começar outra história!"
        # e IMEDIATAMENTE iniciar a história
        historia(ctx)
        return

    # caso normal
    ctx.memory.story_step = choice["next_step"]




# ─────────────────────────────────────────
# WRAPPERS DE OPÇÕES (SEM LÓGICA)
# ─────────────────────────────────────────
def sim(ctx):
    # 1️⃣ se há escolha pendente → resolver escolha
    if ctx.memory.pending_choice:
        escolha(ctx)
        return

    # 2️⃣ se não há escolha, "sim" equivale a pedir história
    ctx.intent_executed = "historia"
    ctx.memory.mode = "story"
    ctx.memory.story_step = 0
    ctx.memory.current_story = None
    historia(ctx)



def nao(ctx):
    escolha(ctx)


def voar(ctx):
    escolha(ctx)

def esperar(ctx):
    escolha(ctx)


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

        # 🔑 criar escolha SIM / NÃO
        ctx.memory.pending_choice = {
            "domain": "historia",
            "next_step": 0,
            "options": {
                "sim": "nova_historia",
                "nao": "fim_definitivo"
            }
        }

        ctx.memory.mode = None
        ctx.memory.story_step = 0
        return

    ctx.memory.story_step += 1



# ─────────────────────────────────────────
# OUTROS HANDLERS
# ─────────────────────────────────────────

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
    if ctx.memory.mode == "story":
        ctx.intent_executed = "historia"
        historia(ctx)
    else:
        ctx.response_type = "confirmado"


def negacao(ctx):
    if ctx.memory.mode == "story":
        ctx.memory.mode = None
        ctx.response_type = "recusou"
    else:
        ctx.response_type = "negou"
