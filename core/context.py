#context.py

from state.state import State
from state.memory import Memory

class Context:
    def __init__(self, texto):
        # INPUT
        self.raw_text = texto
        self.text = None

        # INTENÇÕES
        self.detected_intents = []
        self.intent_detected = None
        self.intent_executed = None

        # ESTADO E MEMÓRIA (NUNCA None)
        self.state = State()
        self.memory = Memory()

        # RESPOSTA
        self.response_type = "default"
        self.response_text = None

        # DEBUG / TRACE
        self.trace = []

