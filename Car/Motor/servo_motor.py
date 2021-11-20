from adafruit_servokit import ServoKit

from Motor.motor import MotorController


class ServoMotorController(MotorController):

    __straight = 120

    def __init__(self, default_speed: int = 50, max_speed: int = None):
        super().__init__(default_speed, max_speed)
        print("Init Servo Kit")
        self.__servo_kit = ServoKit(channels=16)
        print("Servo Kit Initialized")
        self.__servo_kit.servo[0].angle=ServoMotorController.__straight
        self.__left_max = 90
        self.__right_max = 150
        self.__straight = ServoMotorController.__straight
    
    def getMaxLeft(self):
        return self.__left_max

    def getMaxRight(self):
        return self.__right_max

    def getStraight(self):
        return self.__straight

    def car_steering(self, direction: int = 120):
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
        self.car_steering(self.getMaxLeft())

    def rightsteering(self):
        self.car_steering(self.getMaxRight())

    def straightsteering(self):
        self.car_steering(self.getStraight())
