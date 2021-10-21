import time

import Jetson.GPIO as GPIO


class MotorController:
    _max_speed = 100
    _default_frequency = 50

    def __init__(self, default_speed: int = 50, max_speed: int = None):
        self._motors = {}
        self._default_speed = default_speed
        if self._max_speed is None:
            self._max_speed = MotorController._max_speed
        else:
            self._max_speed = max_speed
        GPIO.setwarnings(False)

    def get_default_speed(self):
        return self._default_speed

    def get_max_speed(self):
        return self._max_speed

    @staticmethod
    def get_default_frequency():
        return MotorController._default_frequency

    def add_motor(self, name: str, IN1: str, IN2: str, ENPIN: str, frequency: int = None):
        self._motors[name] = {}
        if frequency is None:
            frequency = MotorController.get_default_frequency()
        self._motors[name]["IN1"] = IN1
        self._motors[name]["IN2"] = IN2
        self._motors[name]["ENPIN"] = ENPIN
        self._motors[name]["PWM"] = frequency
        self._motors[name]["CURRENTSPEED"] = 0
        self._motors[name]["NAME"] = name

    def get_motor(self, name: str):
        return self._motors[name]

    def get_motors(self):
        return self._motors

    def start_motor(self):
        GPIO.setmode(GPIO.TEGRA_SOC)
        for motor in self.get_motors():
            mo = self._motors[motor]
            GPIO.setup(mo["IN1"], GPIO.OUT)
            GPIO.setup(mo["IN2"], GPIO.OUT)
            GPIO.setup(mo["ENPIN"], GPIO.OUT)
            mo["MotorControl"] = GPIO.PWM(mo["ENPIN"], mo["PWM"])
            mo["MotorControl"].start(0)

    def car_move_direction(self, motors, speed, forwarddirection: bool, duration: int = 0):
        try:
            for name in motors:
                self.set_motor_direction(name, forwarddirection)
                self.set_motor_control_speed(name, speed)
            if duration > 0:
                time.sleep(duration)
                self.stop()
        except:
            self.stop()
            raise
                    
    def car_move_forwards(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_direction(self.get_motors(), speed, True, duration)

    def car_move_backwards(self, speed: int = None, duration: int = 0):
        if speed is None:
            speed = self.get_default_speed()
        self.car_move_direction(self.get_motors(), speed, False, duration)
    
    def get_motor_control(self, name):
        return self._motors[name]["MotorControl"]

    def set_motor_speed(self, name, speed):
        self._motors[name]["CURRENTSPEED"] = speed

    def get_motor_speed(self, name):
        return self._motors[name]["CURRENTSPEED"]

    def set_motor_control_speed(self, name, speed):
        control = self.get_motor_control(name)
        if speed > self.get_max_speed():
            speed = self.get_max_speed()
        self.set_motor_speed(name, speed)
        control.ChangeDutyCycle(speed)

    def set_motor_direction(self, name: str, forward: bool):
        motor = self.get_motor(name)
        if forward:
            GPIO.output(motor["IN1"], True)
            GPIO.output(motor["IN2"], False)
        else:
            GPIO.output(motor["IN1"], False)
            GPIO.output(motor["IN2"], True)

    def accelerate_car(self, acceleration: int = 1):
        for motor in self.get_motors():
            self.accelerate_motor(motor, acceleration)

    def brake_car(self, brake: int = 1):
        for motor in self.get_motors():
            self.brake_motor(motor, brake)

    def accelerate_motor(self, name: str, acceleration: int = 1):
        current_speed = self.get_motor_speed(name)
        new_speed = current_speed + acceleration
        if new_speed > self.get_max_speed():
            new_speed = self.get_max_speed()
        self.set_motor_control_speed(name, new_speed)

    def brake_motor(self, name: str, brake: int = 1):
        current_speed = self.get_motor_speed(name)
        new_speed = current_speed - brake
        if new_speed < 0:
            new_speed = 0
        self.set_motor_control_speed(name, new_speed)

    def stop(self):
        motors = self.get_motors()
        for motor_name in motors:
            self.get_motor_control(motor_name).ChangeDutyCycle(0)

    def stop_motor(self):
        GPIO.cleanup()
