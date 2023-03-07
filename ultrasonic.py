# ultrasound.py
import pigpio
import time
from pins import *


def get_distance(trigger_pin, echo_pin):
    pi = pigpio.pi()

    # Sending the ultrasound signal
    pi.write(trigger_pin, 0)
    time.sleep(0.0001)
    pi.write(trigger_pin, 1)
    time.sleep(0.00001)
    pi.write(trigger_pin, 0)

    # Waiting for the echo signal
    start = time.time()
    while pi.read(echo_pin) == 0:
        start = time.time()
    while pi.read(echo_pin) == 1:
        stop = time.time()

    # Calculate the distance
    elapsed = stop - start
    distance = elapsed * 34300 / 2  # 34300 = Speed of sound in cm/s
    distance = round(distance, 2)

    pi.stop()

    return distance


def get_distances():
    distances = {
        "left": get_distance(PIN_US_LEFT_TRIGGER, PIN_US_LEFT_ECHO),
        "middle": get_distance(PIN_US_MIDDLE_TRIGGER, PIN_US_MIDDLE_ECHO),
        "right": get_distance(PIN_US_RIGHT_TRIGGER, PIN_US_RIGHT_ECHO),
    }
    return distances