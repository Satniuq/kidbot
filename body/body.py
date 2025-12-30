from expressions import EXPRESSIONS
import leds


def actualizar_corpo(state):
    emocao = state.get("emocao", "neutro")
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
