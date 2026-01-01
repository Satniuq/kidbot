#brain.py

from core.context import Context
from core.pipeline import processar
from core.pipeline_steps import PIPELINE

def pensar(texto, agent):
    ctx = Context(texto)

    session = agent.new_episode()

    # injectar sessão
    ctx.state = session.state
    ctx.memory = session.memory

    processar(ctx, PIPELINE)
    return ctx
