from core.brain import pensar
from core.agent import Agent   # ou o teu agente real

def run_dialogue(inputs):
    agent = Agent()
    outputs = []

    for text in inputs:
        ctx = pensar(text, agent)
        outputs.append({
            "input": text,
            "intent": ctx.intent_executed,
            "response_type": ctx.response_type,
            "response": ctx.response_text
        })

    return outputs
