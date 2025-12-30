import subprocess
import tempfile
import os

WHISPER_BIN = "/home/satniuq/whisper.cpp/build/bin/whisper-cli"
WHISPER_MODEL = "/home/satniuq/whisper.cpp/models/ggml-tiny.bin"
AUDIO_DEVICE = "plughw:3,0"

def ouvir(duracao=4):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav_path = f.name

    try:
        # Grava áudio com duração fixa
        subprocess.run(
            [
                "arecord",
                "-D", AUDIO_DEVICE,
                "-f", "S16_LE",
                "-r", "16000",
                "-c", "1",
                "-d", str(duracao),
                wav_path
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )

        # Executa Whisper
        result = subprocess.run(
            [
                WHISPER_BIN,
                "-m", WHISPER_MODEL,
                "-f", wav_path,
                "-l", "pt",
                "--no-timestamps",
                "-t", "2"
            ],
            capture_output=True,
            text=True
        )

        # O texto reconhecido vem no stdout
        texto = result.stdout.strip()
        return texto if texto else None

    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)
