import time
import RPi.GPIO as GPIO

LED_ESQ = 17
LED_DIR = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_ESQ, GPIO.OUT)
GPIO.setup(LED_DIR, GPIO.OUT)


def olhos_on():
    GPIO.output(LED_ESQ, GPIO.HIGH)
    GPIO.output(LED_DIR, GPIO.HIGH)


def olhos_off():
    GPIO.output(LED_ESQ, GPIO.LOW)
    GPIO.output(LED_DIR, GPIO.LOW)


def olhos_piscar(vezes=3, intervalo=0.3):
    for _ in range(vezes):
        olhos_on()
        time.sleep(intervalo)
        olhos_off()
        time.sleep(intervalo)


def olhos_lento():
    olhos_on()
    time.sleep(1)
    olhos_off()
    time.sleep(1)
