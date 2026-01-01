#main.py

from core.agent import Agent
from core.brain import pensar
from interface.tts import falar
from body.body import actualizar_corpo

agent = Agent()

while True:
    texto = input("> ")

    ctx = pensar(texto, agent)

    # fala a resposta
    falar(ctx.response_text)

    # corpo reage ao ESTADO
    actualizar_corpo(ctx.state)
