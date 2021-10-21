from Motor.motor import MotorController

servo_motor = MotorController(default_speed=50, max_speed=100)
servo_motor.add_motor("HINTEN", 35, 36, 33, 100)
servo_motor.start_motor()
servo_motor.car_move_forwards(50, 1.0)
# servo_motor.stop()
servo_motor.stop_motor()
