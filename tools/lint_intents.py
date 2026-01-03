from collections import defaultdict

from language.intents import INTENTS
import decision.handlers as handlers


# ─────────────────────────────────────────
# 1️⃣ Conflitos lexicais
# ─────────────────────────────────────────
def check_lexical_conflicts():
    """
    Detecta tokens (patterns) que aparecem em mais do que um intent.
    Exemplo perigoso: 'ajuda' em 'ajuda' e 'esperar'
    """
    token_map = defaultdict(set)

    for intent, data in INTENTS.items():
        patterns = data.get("patterns", [])
        for pattern in patterns:
            token_map[pattern].add(intent)

    conflicts = {
        token: intents
        for token, intents in token_map.items()
        if len(intents) > 1
    }

    return conflicts


# ─────────────────────────────────────────
# 2️⃣ Intents sem handler
# ─────────────────────────────────────────
def check_missing_handlers():
    """
    Verifica se todos os intents têm um handler correspondente.
    """
    handler_names = {
        name for name in dir(handlers)
        if not name.startswith("_")
    }

    missing = [
        intent for intent in INTENTS
        if intent not in handler_names
    ]

    return missing


# ─────────────────────────────────────────
# 3️⃣ Runner principal
# ─────────────────────────────────────────
def run_lint():
    errors = False

    # ── conflitos lexicais ──
    conflicts = check_lexical_conflicts()
    if conflicts:
        errors = True
        print("❌ Conflitos lexicais detectados:")
        for token, intents in conflicts.items():
            intents_list = ", ".join(sorted(intents))
            print(f"   • '{token}' → {intents_list}")

    # ── intents sem handler ──
    missing = check_missing_handlers()
    if missing:
        errors = True
        print("❌ Intents sem handler correspondente:")
        for intent in missing:
            print(f"   • {intent}")

    if not errors:
        print("✅ Lint passou sem erros")

    return not errors


# ─────────────────────────────────────────
# 4️⃣ Execução directa
# ─────────────────────────────────────────
if __name__ == "__main__":
    ok = run_lint()
    if not ok:
        exit(1)
