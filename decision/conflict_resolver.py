# decision/conflict_resolver.py

from language.intents import INTENTS


DOMAIN_META = "META"
DOMAIN_STORY = "STORY"
DOMAIN_SOCIAL = "SOCIAL"


def _normalizar_intent(i):
    """
    Normaliza um intent para formato interno comum.
    Aceita:
      - string
      - dict semântico vindo do matcher
    """
    if isinstance(i, str):
        data = INTENTS.get(i, {})
        return {
            "name": i,
            "domain": data.get("domain"),
            "priority": data.get("priority", 0),
            "acts": data.get("acts", []),
            "params": {}
        }

    if isinstance(i, dict):
        name = i.get("intent")
        base = INTENTS.get(name, {})
        return {
            "name": name,
            "domain": i.get("domain", base.get("domain")),
            "priority": base.get("priority", 0),
            "acts": i.get("acts", base.get("acts", [])),
            "params": i.get("params", {})
        }

    return None


def resolver(intents, ctx=None):
    """
    Resolve a intenção final com base em:
    1) domínios (META > STORY > SOCIAL)
    2) escolhas pendentes
    3) contexto narrativo
    4) prioridade
    Compatível com intents semânticos.
    """

    if not intents:
        return None

    # normaliza tudo
    norm = [_normalizar_intent(i) for i in intents]
    norm = [i for i in norm if i and i["name"]]

    if not norm:
        return None

    # ─────────────────────────────────────────
    # 1️⃣ META fura tudo
    # ─────────────────────────────────────────
    meta = [i for i in norm if i["domain"] == DOMAIN_META]
    if meta:
        return max(meta, key=lambda i: i["priority"])["name"]

    # ─────────────────────────────────────────
    # 2️⃣ Escolha pendente
    # ─────────────────────────────────────────
    if ctx and ctx.memory.pending_choice:
        for opt in ctx.memory.pending_choice["options"]:
            for i in norm:
                if i["name"] == opt:
                    return opt

    # ─────────────────────────────────────────
    # 3️⃣ STORY com contexto
    # ─────────────────────────────────────────
    story = [i for i in norm if i["domain"] == DOMAIN_STORY]

    if story and ctx:
        # iniciar história é sempre válido
        for i in story:
            if i["name"] == "historia":
                return "historia"

        if ctx.memory.mode == "story":
            # continuar narrativa
            for i in story:
                if i["name"] == "continuar":
                    return "continuar"

            return max(story, key=lambda i: i["priority"])["name"]

    # ─────────────────────────────────────────
    # 4️⃣ SOCIAL
    # ─────────────────────────────────────────
    social = [i for i in norm if i["domain"] == DOMAIN_SOCIAL]
    if social:
        return max(social, key=lambda i: i["priority"])["name"]

    # ─────────────────────────────────────────
    # 5️⃣ Fallback final
    # ─────────────────────────────────────────
    return max(norm, key=lambda i: i["priority"])["name"]
