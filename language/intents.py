# language/intents.py

INTENTS = {

    # ── ESCOLHAS GERAIS (dependem de contexto) ────────────────────────
    "sim": {
        "priority": 10,
        "domain": "STORY",
        "canonical": "confirmar",
        "acts": ["confirmar", "aceitar", "prosseguir"],
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
        "domain": "STORY",
        "canonical": "negar",
        "acts": ["negar", "recusar", "parar"],
        "patterns": [
            "nao",
            "não",
            "nem pensar",
            "agora nao",
            "agora não"
        ]
    },

    # ── SAUDAÇÃO / SOCIAL ────────────────────
    "saudacao": {
        "priority": 1,
        "domain": "SOCIAL",
        "canonical": "saudacao",
        "acts": ["saudar", "oferecer_opcoes"],
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

    # ── META / AJUDA ────────────────────
    "ajuda": {
        "priority": 1,
        "domain": "META",
        "canonical": "ajuda",
        "acts": ["explicar", "oferecer_opcoes", "orientar"],
        "patterns": [
            "o que sabes fazer",
            "ajuda",
            "como funcionas",
            "o que podes fazer"
        ]
    },

    # ── HISTÓRIA (entrada / progressão) ─────────────────────────────
    "historia": {
        "priority": 2,
        "domain": "STORY",
        "canonical": "historia",
        "acts": ["iniciar", "continuar", "narrar"],
        "patterns": [
            "historia",
            "conta uma historia",
            "conta-me uma historia",
            "quero uma historia",
            "historias"
        ]
    },

    # Normalização semântica: "mais", "depois", etc são tudo "continuar"
    "continuar": {
        "priority": 2,
        "domain": "STORY",
        "canonical": "continuar",
        "acts": ["continuar", "prosseguir"],
        "patterns": [
            "continua",
            "mais",
            "e depois",
            "e a seguir",
            "depois"
        ]
    },

    # ── META / CONTROLO ────────────────────
    "parar": {
        "priority": 4,
        "domain": "META",
        "canonical": "parar",
        "acts": ["interromper", "terminar"],
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
        "domain": "STORY",
        "canonical": "voar",
        "acts": ["escolha"],
        "patterns": [
            "voar",
            "tentar voar",
            "voa",
            "voe"
        ]
    },

    "esperar": {
        "priority": 10,
        "domain": "STORY",
        "canonical": "esperar",
        "acts": ["escolha"],
        "patterns": [
            "esperar",
            "espera",
            "aguardar"
        ]
    },

    # ── IDENTIDADE / META ────────────────────
    "identidade": {
        "priority": 3,
        "domain": "META",
        "canonical": "identidade",
        "acts": ["apresentar", "explicar"],
        "patterns": [
            "quem es",
            "quem és",
            "o que es",
            "diz quem es"
        ]
    },

    # ── DESPEDIDA / SOCIAL ────────────────────
    "despedida": {
        "priority": 1,
        "domain": "SOCIAL",
        "canonical": "despedida",
        "acts": ["despedir"],
        "patterns": [
            "adeus",
            "tchau",
            "ate logo",
            "xau"
        ]
    },
}
