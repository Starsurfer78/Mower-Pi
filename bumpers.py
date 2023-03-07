import pigpio
from pins import *

def read_bumpers():
    # Initialise the GPIO
    pi = pigpio.pi()

    # Set the pull-up resistor for the pins
    pi.set_pull_up_down(PIN_LEFT_BUMPER, pigpio.PUD_UP)
    pi.set_pull_up_down(PIN_RIGHT_BUMPER, pigpio.PUD_UP)

    # Read the status of the microswitches
    left_bumper = not pi.read(PIN_LEFT_BUMPER)
    right_bumper = not pi.read(PIN_RIGHT_BUMPER)

    # Terminate the connection to the GPIO
    pi.stop()

    return left_bumper, right_bumper
