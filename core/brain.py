from core.context import Context
from core.pipeline import processar
from core.pipeline_steps import PIPELINE
from core.agent import Agent

agent = Agent()


def pensar(texto):
    ctx = Context(texto)

    session = agent.new_episode()

    # injectar sessão no episódio
    ctx.state = session.state
    ctx.memory = session.memory

    processar(ctx, PIPELINE)
    return ctx.response_text
