from adafruit_servokit import ServoKit

from Motor.motor import MotorController


class ServoMotorController(MotorController):

    def __init__(self, default_speed: int = 50, max_speed: int = None):
        super().__init__(default_speed, max_speed)
        self.__servo_kit = ServoKit(channels=16)
        self.__servo_kit.servo[0].angle=120
        self.__left_max = 95
        self.__right_max = 150
        self.__straight = 115
    
    def getMaxLeft(self):
        return self.__left_max

    def getMaxRight(self):
        return self.__right_max

    def getStraight(self):
        return self.__straight

    def car_steering(self, direction: int = 115):
        try:
            if (direction > self.getMaxRight()):
                direction = self.getMaxRight()
            if (direction < self.getMaxLeft()):
                direction = self.getMaxLeft()
            self.__servo_kit.servo[0].angle=direction
        except:
            self.stop()
            raise

    def leftsteering(self):
        print("event left")
        self.car_steering(self.getMaxLeft())

    def rightsteering(self):
        print("event right")
        self.car_steering(self.getMaxRight())

    def straightsteering(self):
        print("event straight")
        self.car_steering(self.getStraight())
