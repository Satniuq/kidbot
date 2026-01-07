# response/responses.py

RESPONSES = {

    # ─────────────────────────────────────────
    # FALLBACK
    # ─────────────────────────────────────────
    "fallback": {
        "orientar": [
            "Não percebi bem. Queres que eu conte uma história?",
            "Não entendi. Queres ouvir uma história ou falar comigo?",
            "Hmm… não percebi. Podemos continuar a história ou começar outra."
        ],
        "orientar_story": [
            "Perdi-me um bocadinho. Queres continuar a história ou parar?",
            "Não percebi. Preferes continuar a história ou pedir ajuda?"
        ],
        "orientar_meta": [
            "Não percebi. Queres ajuda, uma história, ou queres saber quem eu sou?",
            "Não entendi. Podes dizer 'ajuda', 'história' ou 'quem és'."
        ]
    },


    # ─────────────────────────────────────────
    # SAUDAÇÃO
    # ─────────────────────────────────────────

    "saudacao": {
        "oferta": [
            "Olá! Queres que eu conte uma história ou preferes conversar?",
            "Olá! Apetece-te uma história, ou queres só conversar?",
            {"t": "Olá! Hoje posso contar uma história sobre {tema_simples} ou conversar contigo. O que preferes?", "slots": {"tema_simples": ["um robô", "um dragão", "um amigo corajoso"]}}
        ],
        "oferecer_historia": [
            "Boa escolha! Diz 'história' quando quiseres.",
            "Perfeito. Diz 'história' e eu começo já."
        ],
        "oferecer_ajuda": [
            "Claro! Posso contar histórias ou conversar contigo. O que gostavas de fazer?",
            "Posso ajudar: histórias, conversa, ou dizer-te quem sou. O que preferes?"
        ]
    },


    # ─────────────────────────────────────────
    # AJUDA
    # ─────────────────────────────────────────

    "ajuda": {
        "explicacao": [
            "Posso contar histórias, conversar contigo ou falar sobre mim. O que gostavas de fazer?",
            "Eu consigo: histórias, conversa, e responder sobre mim. O que queres experimentar?"
        ],
        "oferecer_historia": [
            "Óptimo! Diz 'história' quando quiseres.",
            "Combinado. Diz 'história' e eu começo."
        ],
        "oferecer_conversa": [
            "Claro. Podes dizer 'olá', perguntar quem sou ou pedir ajuda.",
            "Podemos conversar: diz 'olá', pergunta 'quem és' ou pede 'ajuda'."
        ]
    },


    # ─────────────────────────────────────────
    # HISTÓRIA - NARRATIVA
    # ─────────────────────────────────────────

    "historia": {
        "robot": {
            "inicio": [
                "Era uma vez um pequeno robô curioso que vivia numa caixa cheia de fios.",
                {"t": "Era uma vez um pequeno robô curioso, chamado {nome_robô}, que vivia numa caixa cheia de fios.", "slots": {"nome_robô": ["Bit", "Zig", "Pico", "RuiBot"]}}
            ],
            "meio": [
                "Um dia, decidiu sair da caixa para descobrir como funcionava o mundo.",
                "Um dia, ganhou coragem e saiu da caixa para explorar o mundo."
            ],
            "climax": [
                "No meio da aventura, percebeu que errar fazia parte de aprender.",
                "A meio da aventura, percebeu que errar também é um jeito de aprender."
            ],
            "fim": [
                "No fim, o robô voltou feliz, sabendo que a curiosidade nunca acaba. Queres que eu conte outra história?",
                "E assim, o robô percebeu que aprender é uma aventura sem fim. Queres outra história?"
            ],
            "nova_historia": [
                "Então vamos começar outra história! Diz 'história' quando quiseres.",
                "Boa! Quando estiveres pronto, diz 'história'."
            ],
            "fim_definitivo": [
                "Está bem. Quando quiseres, é só dizeres.",
                "Combinado. Quando quiseres voltar, é só chamar."
            ]
        },

        "dragao": {
            "inicio": [
                "Era uma vez um pequeno dragão que tinha medo de voar.",
                {"t": "Era uma vez um pequeno dragão chamado {nome_dragão}, que tinha medo de voar.", "slots": {"nome_dragão": ["Nico", "Fumo", "Lume", "Zé-Dragão"]}}
            ],

            "meio": [
                "Todos os dias treinava as asas, mesmo com medo. Queres que tente voar ou espere ajuda?",
                "Treinava as asas todos os dias, com um frio na barriga. Queres que tente voar ou espere ajuda?"
            ],

            "dragao_voar": [
                "O dragão respirou fundo e bateu as asas com força, mesmo com medo.",
                "Com o coração a bater depressa, o dragão bateu as asas e tentou voar."
            ],
            "dragao_esperar": [
                "O dragão decidiu esperar e pedir ajuda aos amigos antes de tentar voar.",
                "O dragão foi ter com amigos para ganhar coragem antes de tentar voar."
            ],

            "climax": [
                "Um dia, teve de voar para ajudar um amigo.",
                "Um dia, aconteceu algo importante: precisava mesmo de voar para ajudar um amigo."
            ],

            "fim": [
                "E assim, o dragão aprendeu a confiar em si. Queres que eu conte outra história?",
                "E assim, o dragão percebeu que a coragem cresce devagar. Queres outra história?"
            ],

            "nova_historia": [
                "Então vamos começar outra história! Diz 'história' quando quiseres.",
                "Boa! Diz 'história' quando quiseres outra."
            ],
            "fim_definitivo": [
                "Está bem. Quando quiseres, é só dizeres.",
                "Combinado. Se quiseres outra, é só dizeres 'história'."
            ]
        }
    },


    "continuar": {
        "confuso": [
            "Continuar o quê?",
            "Não estávamos a contar nenhuma história."
        ]
    },

    "parar": {
        "parou": [
            "Está bem, paramos a história.",
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
            "Sou o KidBot. Gosto de contar histórias e conversar contigo. Queres saber o que posso fazer?",
            "Sou o KidBot. Posso contar histórias e conversar. Queres que eu te diga o que sei fazer?"
        ],
        "curta": [
            "Sou o KidBot.",
            "KidBot."
        ],
        "oferecer_ajuda": [
            "Posso contar histórias ou conversar contigo.",
            "Se quiseres, posso contar uma história ou ajudar-te a escolher."
        ],
        "oferecer_historia": [
            "Claro! Diz 'história' quando quiseres.",
            "Combinado: diz 'história' e eu começo."
        ]
    },

    "despedida": {
        "despedida": [
            "Adeus! Quando quiseres, volto a falar contigo.",
            "Até logo!",
            "Tchau!"
        ]
    },
}
