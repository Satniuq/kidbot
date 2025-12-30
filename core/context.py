class Context:
    def __init__(self, texto):
        # INPUT
        self.raw_text = texto
        self.text = None  # texto normalizado

        # INTENÇÕES
        self.detected_intents = []
        self.intent = None

        # ESTADO INTERNO
        self.state = None
        self.memory = None

        # RESPOSTA
        self.response_type = None
        self.response_text = None
