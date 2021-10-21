import time

from Motor.motor import MotorController


class BotMotorController(MotorController):

    def add_motor(self, name: str, IN1: int, IN2: int, ENPIN: int, front: bool, left: bool, PWM: int = None):
        if PWM is None:
            PWM = self._max_speed
        super().add_motor(name, IN1, IN2, ENPIN, PWM)
        self._motors[name]["FRONT"] = front
        self._motors[name]["LEFT"] = left

    def car_move_leftright_direction(self, speed: int = None, forwarddirection: bool = True, leftdirection: bool = True, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        motors = self.get_motors()
        try:
            for motor in motors:
                mo = self.get_motor(motor)
                if forwarddirection:
                    if mo["LEFT"] is not leftdirection:
                        self.set_motor_direction(motor, True)
                        self.set_motor_control_speed(motor, speed)
                    else:
                        self.set_motor_control_speed(motor, 0)
                else:
                    if mo["LEFT"] is leftdirection:
                        self.set_motor_direction(motor, False)
                        self.set_motor_control_speed(motor, speed)
                    else:
                        self.set_motor_control_speed(motor, 0)
            
            if duration > 0:
                time.sleep(duration)
                self.stop()
        except:
            self.stop()
            raise

    def car_move_right(self, speed: int = None, forwarddirection: bool = True, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_leftright_direction(speed, forwarddirection, False, duration)

    def car_move_left(self, speed: int = None, forwarddirection: bool = True, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_leftright_direction(speed, forwarddirection, True, duration)

    def car_move_forward_right(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_right(speed, True, duration)

    def car_move_forward_left(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_left(speed, True, duration)

    def car_move_backwards_right(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_right(speed, False, duration)

    def car_move_backwards_left(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_left(speed, False, duration)

    

