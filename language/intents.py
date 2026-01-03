#intents.py

INTENTS = {

    # ── ESCOLHAS GERAIS ────────────────────────
    "sim": {
        "priority": 10,
        "patterns": [
            "sim",
            "claro",
            "ok",
            "está bem",
            "esta bem",
            "quero"
        ]
    },

    "nao": {
        "priority": 10,
        "patterns": [
            "nao",
            "não",
            "nem pensar",
            "agora nao",
            "agora não"
        ]
    },

    # ── SAUDAÇÃO ────────────────────
    "saudacao": {
        "priority": 1,
        "patterns": [
            "ola",
            "oi",
            "bom dia",
            "boa tarde",
            "conversar",
            "falar",
            "fala",
            "vamos conversar"
        ]
    },


    # ── AJUDA ────────────────────
    
    "ajuda": {
        "priority": 1,
        "patterns": [
            "o que sabes fazer",
            "ajuda",
            "como funcionas",
            "o que podes fazer"
        ]
    },

    # ── HISTÓRIA ─────────────────────────────
    "historia": {
        "priority": 2,
        "patterns": [
            "historia",
            "conta uma historia",
            "conta-me uma historia",
            "quero uma historia",
            "historias"
        ]
    },

    "continuar": {
        "priority": 2,
        "patterns": [
            "continua",
            "mais",
            "e depois",
            "e a seguir",
            "depois"
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

    # ── HISTÓRIA - ESCOLHAS NARRATIVAS ────────────────────
    "voar": {
        "priority": 10,
        "patterns": [
            "voar",
            "tentar voar",
            "voa",
            "voe"
        ]
    },

    "esperar": {
        "priority": 10,
        "patterns": [
            "esperar",
            "espera",
            "aguardar"
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



    "despedida": {
        "priority": 1,
        "patterns": [
            "adeus",
            "tchau",
            "ate logo",
            "xau"
        ]
    },
}
