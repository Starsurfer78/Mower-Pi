# pins.py

# Ultrasonic Sensors
PIN_US_LEFT_TRIGGER = 17
PIN_US_LEFT_ECHO = 18
PIN_US_MIDDLE_TRIGGER = 22
PIN_US_MIDDLE_ECHO = 23
PIN_US_RIGHT_TRIGGER = 24
PIN_US_RIGHT_ECHO = 25

# Motor Control
PIN_LEFT_MOTOR_EN = 5
PIN_LEFT_MOTOR_IN1 = 6
PIN_LEFT_MOTOR_IN2 = 13

PIN_RIGHT_MOTOR_EN = 12
PIN_RIGHT_MOTOR_IN1 = 16
PIN_RIGHT_MOTOR_IN2 = 20

PIN_MOW_MOTOR_EN = 21
PIN_MOW_MOTOR_IN1 = 19
PIN_MOW_MOTOR_IN2 = 26

# Bumper
PIN_LEFT_BUMPER = 17
PIN_RIGHT_BUMPER = 27

# PID-Parameter
KP = 0.5
KI = 0.1
KD = 0.2

# Kalman-Filter-Parameter
Q = 0.001
R = 0.1
X0 = 0
P0 = 1
