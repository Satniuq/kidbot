from .helpers import run_dialogue

def test_historia_completa():
    dialogue = run_dialogue([
        "ola",
        "historia",
        "continua",
        "continua",
        "sim",
        "historia"
    ])

    # entrou em modo história
    assert dialogue[1]["intent"] == "historia"

    # última resposta é narrativa válida (não fallback)
    assert dialogue[-1]["intent"] == "historia"
    assert dialogue[-1]["response"] is not None
    assert dialogue[-1]["response"] != "Não sei bem o que dizer."

