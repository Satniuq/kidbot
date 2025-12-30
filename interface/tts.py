import subprocess

PIPER = "piper-tts"
MODEL = "voices/pt_PT_tugao/model.onnx"
CONFIG = "voices/pt-PT-tugao/pt_PT-tugão-medium.onnx.json"

def falar(texto: str):
    if not texto:
        return

    piper = subprocess.Popen(
        [
            PIPER,
            "-m", MODEL,
            "-c", CONFIG,
            "--output_raw",
            "--quiet"
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )

    aplay = subprocess.Popen(
        [
            "aplay",
            "-f", "S16_LE",
            "-r", "22050",
            "-c", "1"
        ],
        stdin=piper.stdout,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    piper.stdin.write(texto.encode("utf-8"))
    piper.stdin.close()

    piper.wait()
    aplay.wait()
