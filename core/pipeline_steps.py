from language.normalizer import normalizar
from language.intent_matcher import detectar_intencoes
from decision.conflict_resolver import resolver
from decision import handlers
from decision.policy import aplicar_politica
from response.picker import escolher_resposta
from state.state import State
from state.memory import Memory


def normalizar_texto(ctx):
    ctx.text = normalizar(ctx.raw_text)


def detectar(ctx):
    ctx.detected_intents = detectar_intencoes(ctx.text)


def escolher_intencao(ctx):
    ctx.intent = resolver(ctx.detected_intents)


def preparar_estado(ctx):
    pass



def aplicar_handler(ctx):
    if ctx.intent:
        handler = getattr(handlers, ctx.intent)
        handler(ctx)


def politica(ctx):
    aplicar_politica(ctx)


def resposta(ctx):
    ctx.response_text = escolher_resposta(
        ctx.intent,
        ctx.response_type
    )
    ctx.memory.last_intent = ctx.intent


PIPELINE = [
    normalizar_texto,
    preparar_estado,
    detectar,
    escolher_intencao,
    aplicar_handler,
    politica,
    resposta
]
