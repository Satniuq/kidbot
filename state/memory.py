# state/memory.py

class Memory:
    def __init__(self):
        # ─────────────────────────────────────────
        # INTENÇÕES
        # ─────────────────────────────────────────
        self.last_intent = None
        self.intent_counts = {}
        self.intent_history = []

        # ─────────────────────────────────────────
        # CONTEXTO
        # ─────────────────────────────────────────
        self.mode = None
        self.current_story = None
        self.pending_choice = None
        self.story_step = 0

        # ─────────────────────────────────────────
        # EMOÇÃO (PERSISTENTE) — pode ficar, não atrapalha
        # ─────────────────────────────────────────
        self.emocao_atual = "neutro"
        self.emocao_history = []

        # ─────────────────────────────────────────
        # MEMÓRIA SEMÂNTICA LEVE (FASE 4)
        # ─────────────────────────────────────────

        # última resposta escolhida (para evitar repetição directa)
        self.last_response_text = None
        self.last_response_type = None

        # contadores por acto (response_type) e por intent
        # ex: acts_count["ajuda"]["explicacao"] = 3
        self.acts_count = {}

        # ofertas feitas / recusas (muito simples, mas útil)
        self.offers_made = {"historia": 0, "ajuda": 0, "conversa": 0}
        self.refusals = {"historia": 0}


    def register_intent(self, intent):
        if intent is None:
            return

        self.last_intent = intent
        self.intent_counts[intent] = self.intent_counts.get(intent, 0) + 1

        self.intent_history.append(intent)
        if len(self.intent_history) > 5:
            self.intent_history.pop(0)


    def register_act(self, intent, response_type):
        """
        Regista o acto executado (aproximado pelo response_type).
        Isto dá base para amplitude: variar respostas e evitar repetição.
        """
        if not intent or not response_type:
            return

        if intent not in self.acts_count:
            self.acts_count[intent] = {}

        self.acts_count[intent][response_type] = self.acts_count[intent].get(response_type, 0) + 1

        self.last_response_type = response_type

        # heurísticas simples (podem ser refinadas depois)
        if intent == "saudacao" and response_type == "oferta":
            self.offers_made["conversa"] += 1
        if intent == "ajuda" and response_type == "explicacao":
            self.offers_made["ajuda"] += 1
        if intent == "historia" and response_type == "fim_definitivo":
            self.refusals["historia"] += 1


    def set_emocao(self, emocao):
        if emocao == self.emocao_atual:
            return

        self.emocao_atual = emocao

        self.emocao_history.append(emocao)
        if len(self.emocao_history) > 5:
            self.emocao_history.pop(0)
