# formatter.py

EMOJI_POR_EMOCAO = {
    "feliz": "😊",
    "confuso": "🤔",
    "neutro": ""
}


def aplicar_emocao(texto, emocao):
    """
    Ajusta o tom final da resposta com base na emoção.
    """
    emoji = EMOJI_POR_EMOCAO.get(emocao, "")
    if emoji:
        return f"{texto} {emoji}"
    return texto


def formatar_resposta(ctx, texto_base):
    """
    Formata a resposta final do bot.
    """
    emocao = ctx.memory.emocao_atual
    return aplicar_emocao(texto_base, emocao)
