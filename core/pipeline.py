#pipeline.py

def processar(context, steps):
    for step in steps:
        context.trace.append(step.__name__)
        step(context)
    return context
