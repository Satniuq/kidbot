class Memory:
    def __init__(self):
        # última intenção detectada (compatível com código existente)
        self.last_intent = None

        # quantas vezes cada intenção ocorreu
        self.intent_counts = {}

        # histórico curto das últimas intenções
        self.intent_history = []

        # modo actual do bot (ex: "story", "chat", None)
        self.mode = None

        # história actualmente em curso (ex: "robot", "dragao")
        self.current_story = None

    def register_intent(self, intent):
        if intent is None:
            return

        # última intenção
        self.last_intent = intent

        # contador por intenção
        self.intent_counts[intent] = self.intent_counts.get(intent, 0) + 1

        # histórico (máx 5)
        self.intent_history.append(intent)
        if len(self.intent_history) > 5:
            self.intent_history.pop(0)
