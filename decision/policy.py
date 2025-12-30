def aplicar_politica(ctx):
    if ctx.state.emocao == "cansado":
        ctx.response_type = "curta"
