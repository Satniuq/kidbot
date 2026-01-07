#pipeline_steps.py

from language.normalizer import normalizar
from language.intent_matcher import detectar_intencoes
from decision.conflict_resolver import resolver
from decision import handlers
from decision.policy import aplicar_politica
from response.picker import escolher_resposta
from state.state import State
from state.memory import Memory
from response.formatter import formatar_resposta


def normalizar_texto(ctx):
    ctx.text = normalizar(ctx.raw_text)
    print("RAW:", repr(ctx.raw_text))
    print("NORM:", repr(ctx.text))



def detectar(ctx):
    ctx.detected_intents = detectar_intencoes(ctx.text)


def escolher_intencao(ctx):
    intent = resolver(ctx.detected_intents, ctx)
    ctx.intent_detected = intent

    if intent is None:
        ctx.intent_executed = "fallback"
    else:
        ctx.intent_executed = intent



def preparar_estado(ctx):
    if ctx.state is None:
        ctx.state = State()

    if ctx.memory is None:
        ctx.memory = Memory()

    if ctx.response_type is None:
        ctx.response_type = "default"



def aplicar_handler(ctx):
    if ctx.intent_executed and hasattr(handlers, ctx.intent_executed):
        handler = getattr(handlers, ctx.intent_executed)
        handler(ctx)




def politica(ctx):
    aplicar_politica(ctx)


def resposta(ctx):
    # sincroniza emoção momentânea → persistente
    if hasattr(ctx.state, "emocao"):
        ctx.memory.set_emocao(ctx.state.emocao)

    texto_base = escolher_resposta(
        ctx.intent_executed,
        ctx.response_type,
        ctx.memory
    )

    ctx.response_text = formatar_resposta(ctx, texto_base)

    ctx.memory.register_intent(ctx.intent_executed)




PIPELINE = [
    normalizar_texto,
    preparar_estado,
    detectar,
    escolher_intencao,
    aplicar_handler,
    politica,
    resposta
]
