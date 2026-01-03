#responses.py

RESPONSES = {

    # ─────────────────────────────────────────
    # FALLBACK
    # ─────────────────────────────────────────
    "fallback": {
        "orientar": [
            "Não percebi bem 😊 Queres que eu conte uma história?",
            "Não entendi 😄 Queres ouvir uma história ou falar comigo?",
            "Hmm… não percebi. Podemos continuar a história ou começar outra 😊"
        ]
    },


    # ─────────────────────────────────────────
    # SAUDAÇÃO
    # ─────────────────────────────────────────

    "saudacao": {
        "oferta": [
            "Olá! 😊 Queres que eu conte uma história ou preferes conversar?"
        ],
        "oferecer_historia": [
            "Boa escolha! 😊 Diz 'história' quando quiseres."
        ],
        "oferecer_ajuda": [
            "Claro! Posso contar histórias ou conversar contigo. O que gostavas de fazer?"
        ]
    },


    # ─────────────────────────────────────────
    # AJUDA
    # ─────────────────────────────────────────

    "ajuda": {
        "explicacao": [
            "Posso contar histórias, conversar contigo ou falar sobre mim. 😊 O que gostavas de fazer?"
        ],
        "oferecer_historia": [
            "Óptimo! 😊 Diz 'história' quando quiseres."
        ],
        "oferecer_conversa": [
            "Claro 😊 Podes dizer 'olá', perguntar quem sou ou pedir ajuda."
        ]
    },


    # ─────────────────────────────────────────
    # HISTÓRIA - NARRATIVA
    # ─────────────────────────────────────────

    "historia": {
        "robot": {
            "inicio": [
                "Era uma vez um pequeno robot curioso que vivia numa caixa cheia de fios."
            ],
            "meio": [
                "Um dia, decidiu sair da caixa para descobrir como funcionava o mundo."
            ],
            "climax": [
                "No meio da aventura, percebeu que errar fazia parte de aprender."
            ],
            "fim": [
                "No fim, o robot voltou feliz, sabendo que a curiosidade nunca acaba. "
                "Queres que eu conte outra história?"
            ],

            # 🔑 resposta ao SIM / NÃO
            "nova_historia": [
                "Então vamos começar outra história! 😊 Diz 'história' quando quiseres."
            ],
            "fim_definitivo": [
                "Está bem. Quando quiseres, é só dizeres 😊"
            ]
        },

        "dragao": {
            "inicio": [
                "Era uma vez um pequeno dragão que tinha medo de voar."
            ],

            "meio": [
                "Todos os dias treinava as asas, mesmo com medo. "
                "Queres que tente voar ou espere ajuda?"
            ],

            "dragao_voar": [
                "O dragão respirou fundo e bateu as asas com força, mesmo com medo."
            ],
            "dragao_esperar": [
                "O dragão decidiu esperar e pedir ajuda aos amigos antes de tentar voar."
            ],

            "climax": [
                "Um dia, teve de voar para ajudar um amigo."
            ],

            "fim": [
                "E assim, o dragão aprendeu a confiar em si. "
                "Queres que eu conte outra história?"
            ],

            # 🔑 resposta ao SIM / NÃO
            "nova_historia": [
                "Então vamos começar outra história! 😊 Diz 'história' quando quiseres."
            ],
            "fim_definitivo": [
                "Está bem. Quando quiseres, é só dizeres 😊"
            ]
        }
    },


    "continuar": {
        "confuso": [
            "Continuar o quê? 😄",
            "Não estávamos a contar nenhuma história."
        ]
    },

    "parar": {
        "parou": [
            "Está bem, paramos a história 😊",
            "Ok, a história fica por aqui."
        ],
        "nada_para": [
            "Não estávamos a contar nenhuma história.",
            "Não há nenhuma história para parar."
        ]
    },

    # ─────────────────────────────────────────
    # IDENTIDADE
    # ─────────────────────────────────────────

    "identidade": {
        "normal": [
            "Sou o KidBot 😊 Gosto de contar histórias e conversar contigo. Queres saber o que posso fazer?"
        ],
        "curta": [
            "Sou o KidBot 😊"
        ],
        "oferecer_ajuda": [
            "Posso contar histórias ou conversar contigo 😊"
        ],
        "oferecer_historia": [
            "Claro! 😊 Diz 'história' quando quiseres."
        ]
    },

    "despedida": {
        "despedida": [
            "Adeus! 😊 Quando quiseres, volto a falar contigo.",
            "Até logo! 👋",
            "Tchau! 😄"
        ]
    },
}
