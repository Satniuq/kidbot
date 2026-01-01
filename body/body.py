#body.py

from body.expressions import EXPRESSIONS
from body import leds


def actualizar_corpo(state):
    # state é um objecto State, não um dict
    emocao = getattr(state, "emocao", "neutro")

    expr = EXPRESSIONS.get(emocao, {})

    olhos = expr.get("olhos")

    if olhos == "on":
        leds.olhos_on()

    elif olhos == "piscar":
        leds.olhos_piscar()

    elif olhos == "lento":
        leds.olhos_lento()

    else:
        leds.olhos_off()

