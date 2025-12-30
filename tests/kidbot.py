from stt_whisper import ouvir
from brain import pensar
from tts import falar

print("🤖 KidBot pronto! Fala comigo...")

while True:
    texto = ouvir(duracao=2)

    if texto:
        print("👉 Ouvi:", texto)

        resposta = pensar(texto)
        if resposta:
            print("🤖 KidBot:", resposta)
            falar(resposta)
