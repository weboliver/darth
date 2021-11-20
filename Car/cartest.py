from Motor.servo_motor import ServoMotorController
from XBoxController.xboxcontroller import XBoxController

xboxController = XBoxController()
servo_motor = ServoMotorController(default_speed=40, max_speed=100)
servo_motor.add_motor("HINTEN", 'UART2_CTS', 'DAP4_FS', 'GPIO_PE6', 50)

from car import Car

newcar = Car("Darth Car", servo_motor, xboxController)
# newcar.add_heartbeat("Camera Observer", 0.5)

newcar.start()
newcar.drive()
print("Ready to drive")
