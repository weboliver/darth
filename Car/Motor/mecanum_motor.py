import time

from Motor.bot_motor import BotMotorController


class MecanumMotorController(BotMotorController):

    def car_slide_direction(self, speed: int = None, duration: int = 0, leftdirection: bool = True):
        if speed is None:
            speed = self.get_max_speed()
        motors = self.get_motors()
        motors_forward = []
        motors_backwards = []
        try:
            for motor in motors:
                mo = self.get_motor(motor)
                if leftdirection:
                    if (mo["FRONT"] is True and mo["LEFT"] is True) or \
                        (mo["FRONT"] is False and mo["LEFT"] is False):
                        motors_backwards.append(motor)
                    else:
                        motors_forward.append(motor)
                else:
                    if (mo["FRONT"] is True and mo["LEFT"] is True) or \
                        (mo["FRONT"] is False and mo["LEFT"] is False):
                        motors_forward.append(motor)
                    else:
                        motors_backwards.append(motor)
                
                for name in motors_forward:
                    self.set_motor_direction(name, True)
                    self.set_motor_control_speed(name, speed)
                for name in motors_backwards:
                    self.set_motor_direction(name, False)
                    self.set_motor_control_speed(name, speed)
            if duration > 0:
                time.sleep(duration)
                self.stop()
        except:
            self.stop()
            raise

    def car_slide_left(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_max_speed()
        self.car_slide_direction(speed, duration, True)

    def car_slide_right(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_max_speed()
        self.car_slide_direction(speed, duration, False)
    
    def car_spin_direction(self, speed: int = None, duration: int = 0, leftdirection: bool = True):
        if speed is None:
            speed = self.get_default_speed()
        motors = self.get_motors()
        motors_forward = []
        motors_backwards = []
        try:
            for motor in motors:
                mo = self.get_motor(motor)
                if mo["LEFT"] is leftdirection:
                    motors_backwards.append(motor)
                else:
                    motors_forward.append(motor)
                for name in motors_forward:
                    self.set_motor_direction(name, True)
                    self.set_motor_control_speed(name, speed)
                for name in motors_backwards:
                    self.set_motor_direction(name, False)
                    self.set_motor_control_speed(name, speed)
            if duration > 0:
                time.sleep(duration)
                self.stop()
        except:
            self.stop()
            raise

    def car_spin_left(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_spin_direction(speed, duration, True)

    def car_spin_right(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_spin_direction(speed, duration, False)

        

    
