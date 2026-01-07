#lint_intent.py
from collections import defaultdict

from language.intents import INTENTS
import decision.handlers as handlers


ALLOWED_DOMAINS = {"META", "STORY", "SOCIAL"}


# ─────────────────────────────────────────
# 1️⃣ Conflitos lexicais
# ─────────────────────────────────────────
def check_lexical_conflicts():
    token_map = defaultdict(set)

    for intent, data in INTENTS.items():
        for pattern in data.get("patterns", []):
            token_map[pattern].add(intent)

    return {
        token: intents
        for token, intents in token_map.items()
        if len(intents) > 1
    }


# ─────────────────────────────────────────
# 2️⃣ Intents sem handler
# ─────────────────────────────────────────
def check_missing_handlers():
    handler_names = {
        name for name in dir(handlers)
        if not name.startswith("_")
    }

    return [
        intent for intent in INTENTS
        if intent not in handler_names
    ]


# ─────────────────────────────────────────
# 3️⃣ Domínios inválidos ou em falta
# ─────────────────────────────────────────
def check_domains():
    errors = []

    for intent, data in INTENTS.items():
        domain = data.get("domain")

        if domain is None:
            errors.append(f"{intent} → domain em falta")
        elif domain not in ALLOWED_DOMAINS:
            errors.append(f"{intent} → domain inválido: {domain}")

    return errors


# ─────────────────────────────────────────
# 4️⃣ Regras semânticas por domínio
# ─────────────────────────────────────────

STORY_KEYWORDS = {
    "historia", "continua", "continuar",
    "voar", "esperar", "depois", "mais"
}

META_KEYWORDS = {
    "ajuda", "parar", "stop",
    "como funcionas", "o que podes fazer"
}

META_VERBS = {
    "para", "parar", "stop", "ajuda"
}


def check_domain_semantics():
    errors = []

    for intent, data in INTENTS.items():
        domain = data.get("domain")
        patterns = data.get("patterns", [])

        # STORY nunca deve ser intent de controlo
        if domain == "STORY" and intent in {"ajuda", "parar", "identidade"}:
            errors.append(
                f"{intent} → STORY não pode ser intent de controlo (META)"
            )

        for p in patterns:
            p_norm = p.lower()
            words = p_norm.split()

            # META pode referir narrativa como objecto de controlo
            if domain == "META" and words and words[0] in META_VERBS:
                continue

            # META não deve conter narrativa como acção
            if domain == "META" and any(k in p_norm for k in STORY_KEYWORDS):
                errors.append(
                    f"{intent} (META) contém padrão narrativo indevido: '{p}'"
                )

            # SOCIAL não deve conter controlo
            if domain == "SOCIAL" and any(k in p_norm for k in META_KEYWORDS):
                errors.append(
                    f"{intent} (SOCIAL) contém padrão de controlo: '{p}'"
                )

    return errors


# ─────────────────────────────────────────
# 5️⃣ Runner principal
# ─────────────────────────────────────────
def run_lint():
    errors = False

    conflicts = check_lexical_conflicts()
    if conflicts:
        errors = True
        print("❌ Conflitos lexicais detectados:")
        for token, intents in conflicts.items():
            print(f"   • '{token}' → {', '.join(sorted(intents))}")

    missing = check_missing_handlers()
    if missing:
        errors = True
        print("❌ Intents sem handler correspondente:")
        for intent in missing:
            print(f"   • {intent}")

    domain_errors = check_domains()
    if domain_errors:
        errors = True
        print("❌ Problemas de domínio:")
        for msg in domain_errors:
            print(f"   • {msg}")

    semantic_errors = check_domain_semantics()
    if semantic_errors:
        errors = True
        print("❌ Problemas semânticos de domínio:")
        for msg in semantic_errors:
            print(f"   • {msg}")

    if not errors:
        print("✅ Lint passou sem erros")

    return not errors


if __name__ == "__main__":
    if not run_lint():
        exit(1)
