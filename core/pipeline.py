def processar(context, steps):
    for step in steps:
        step(context)
    return context
