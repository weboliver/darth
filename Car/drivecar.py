import time

from Motor.servo_motor import ServoMotorController
from Sensoren.hcrsr04 import UltraschallHCRSR04
from Sensoren.sensors import Sensors
from XBoxController.xboxcontroller import XBoxController

sensoren = Sensors()
hcrsr04_sensor1 = UltraschallHCRSR04("UART2_RTS", "SPI2_SCK")

sensoren.add_sensor("HCRSR04", hcrsr04_sensor1)

xboxController = XBoxController()
servo_motor = ServoMotorController(default_speed=60, max_speed=100)
servo_motor.add_motor("HINTEN", 'UART2_CTS', 'DAP4_FS', 'GPIO_PE6', 50)

from car import Car

newcar = Car("Darth Car", servo_motor, xboxController)
newcar.add_heartbeat("Camera Observer", 0.5)
newcar.set_sensors(sensoren)
hcrsr04_sensor1.start()

newcar.start()
newcar.drive()

print("Ready to drive")
