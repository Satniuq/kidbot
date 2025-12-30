# stt_test.py

import subprocess
import json
from vosk import Model, KaldiRecognizer
from brain import pensar
from tts import falar

# =========================
# CONFIGURAÇÃO
# =========================

MODEL_PATH = "models/vosk-model-small-pt-0.3"

# Vosk funciona MUITO melhor a 16000 Hz
SAMPLE_RATE = 16000

# Dispositivo de áudio
AUDIO_DEVICE = "plughw:3,0"

# Flag anti-eco
is_speaking = False

# =========================
# INICIALIZAÇÃO DO STT
# =========================

print("A carregar modelo PT-PT...")
model = Model(MODEL_PATH)

rec = KaldiRecognizer(model, SAMPLE_RATE)

# Menos ruído, decisões mais rápidas
rec.SetWords(False)
rec.SetMaxAlternatives(0)

print("🎤 Fala agora (Ctrl+C para sair)...")

# =========================
# CAPTURA DE ÁUDIO
# =========================

process = subprocess.Popen(
    [
        "arecord",
        "-D", AUDIO_DEVICE,
        "-f", "S16_LE",
        "-r", str(SAMPLE_RATE),
        "-c", "1",
        "-t", "raw"
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL
)

# =========================
# LOOP PRINCIPAL
# =========================

try:
    while True:
        # Enquanto o KidBot fala, ignoramos o micro
        if is_speaking:
            continue

        # Buffer afinado (equilíbrio latência / estabilidade)
        data = process.stdout.read(3200)

        if not data:
            break

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            text = result.get("text", "").strip()

            if text:
                print("👉 Ouvi:", text)

                resposta = pensar(text)

                if resposta:
                    print("🤖 KidBot:", resposta)

                    is_speaking = True
                    falar(resposta)
                    is_speaking = False

except KeyboardInterrupt:
    print("\n⏹️ Interrompido pelo utilizador.")

finally:
    process.terminate()
