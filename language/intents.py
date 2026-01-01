#intents.py

INTENTS = {

    # ── NARRATIVA ─────────────────────────────
    "historia": {
        "priority": 2,
        "patterns": [
            "historia",
            "conta uma historia",
            "conta-me uma historia",
            "quero uma historia"
        ]
    },

    "continuar": {
        "priority": 2,
        "patterns": [
            "continua",
            "mais",
            "e depois",
            "e a seguir"
        ]
    },

    "parar": {
        "priority": 4,
        "patterns": [
            "para",
            "pára",
            "para a historia",
            "ja chega",
            "stop"
        ]
    },

    # ── IDENTIDADE / SOCIAL ────────────────────
    "identidade": {
        "priority": 3,
        "patterns": [
            "quem es",
            "quem és",
            "o que es",
            "diz quem es"
        ]
    },

    "saudacao": {
        "priority": 1,
        "patterns": [
            "ola",
            "oi",
            "bom dia",
            "boa tarde"
        ]
    },

    "despedida": {
        "priority": 1,
        "patterns": [
            "adeus",
            "tchau",
            "ate logo",
            "xau"
        ]
    },

    # ── META / ORIENTAÇÃO ──────────────────────
    "ajuda": {
        "priority": 1,
        "patterns": [
            "o que sabes fazer",
            "ajuda",
            "como funcionas",
            "o que podes fazer"
        ]
    },

    "confirmacao": {
        "priority": 1,
        "patterns": [
            "sim",
            "quero",
            "ok",
            "esta bem"
        ]
    },

    "negacao": {
        "priority": 1,
        "patterns": [
            "nao",
            "não",
            "nao quero",
            "nem pensar"
        ]
    }
}
