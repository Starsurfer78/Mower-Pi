import pigpio
from pins import *

def read_bumpers():
    # Initialisiere den GPIO
    pi = pigpio.pi()

    # Setze den Pull-Up Widerstand für die Pins
    pi.set_pull_up_down(PIN_LEFT_BUMPER, pigpio.PUD_UP)
    pi.set_pull_up_down(PIN_RIGHT_BUMPER, pigpio.PUD_UP)

    # Lese den Zustand der Mikroschalter
    left_bumper = not pi.read(PIN_LEFT_BUMPER)
    right_bumper = not pi.read(PIN_RIGHT_BUMPER)

    # Beende die Verbindung zum GPIO
    pi.stop()

    return left_bumper, right_bumper

