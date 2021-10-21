import time

import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
result = GPIO.PWM(33,100)
result.start(0)
result.ChangeDutyCycle(50)
print(type(result))
GPIO.output(35, True)
GPIO.output(36, False)
print(1)
time.sleep(1.0)
result.stop()
result.start(0)
result.ChangeDutyCycle(50)
print(2)
time.sleep(1.0)
GPIO.cleanup()
