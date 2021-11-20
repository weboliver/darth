import threading
import time

import RPi.GPIO as gpio

from Observer.heartbeat import Heartbeat


class Car:
    def __init__(self, name, motor, controller):
        self._name = name
        self._motorengine = motor
        self._controller = controller
        self._motorevents = {}
        self._hearbeats = {}
        self._sensors = {}
        self._stopped = False
    
    def get_name(self):
        return self._name

    def get_controller(self):
        if self._stopped is False:
            return self._controller
        else:
            return None
    
    def set_sensors(self, sensors):
        self._sensors = sensors

    def get_sensors(self):
        return self._sensors

    def get_heartbeat(self, name):
        return self._hearbeats[name]

    def add_heartbeat(self, name, period):
        self._hearbeats[name] = Heartbeat(name, period)

    def start(self):
        self._stopped = False
        self.get_motorengine().start_motor()
        for heartbeat in self._hearbeats:
            self.get_heartbeat(heartbeat).start()

    def get_motorengine(self):
        return self._motorengine

    def motorevents(self):
        pass

    def handleevent(self, actionevent):
        motor = self.get_motorengine()
        if actionevent["action"] == "forward":
            motor.car_move_forwards()
        elif actionevent["action"] == "backwards":
            motor.car_move_backwards()
        elif actionevent["action"] == "stop":
            motor.stop()
        elif actionevent["action"] == "startmotor":
            motor.start_motor()
        elif actionevent["action"] == "stopcar":
            self.stop()
        elif actionevent["action"] == "leftsteering":
            motor.leftsteering()
        elif actionevent["action"] == "rightsteering":
            motor.rightsteering()
        elif actionevent["action"] == "straightsteering":
            motor.straightsteering()
        elif actionevent["action"] == "moveback_and_steer_right":
            motor.rightsteering()
            motor.car_move_backwards(duration=0.5)
            motor.stop()
            time.sleep(0.5)
            motor.straightsteering()
            time.sleep(0.1)
        else:
            motor.stop()

    def stop(self):
        self._stopped = True
        self.get_motorengine().stop_motor()
        for hearbeat in self._hearbeats:
            self.get_heartbeat(hearbeat).stop()

    def drive(self):
        if self._stopped:
            return
        self.thread = threading.Thread(target=self._drive)
        self.thread.start()

    def _drive(self):
        self._stopped = False
        controller = self.get_controller()
        sensors = self.get_sensors()
        if controller.get_device():
            while True and self._stopped is False:
                if sensors and sensors.has_sensor("HCRSR04"):
                    HCRS04 = sensors.get_sensor("HCRSR04")
                    if HCRS04.get_current_entfernung() > 0 and HCRS04.get_current_entfernung() < 30:
                        print(HCRS04.display_entfernung())
                        actionevent = {}
                        actionevent["action"] = "moveback_and_steer_right"
                    else:
                        actionevent = controller.get_action()
                else:
                    actionevent = controller.get_action()
                if actionevent:
                    self.handleevent(actionevent)
                time.sleep(0.02)
                motor = self.get_motorengine()
                if (motor.get_current_speed()):
                    motor.accelerate(1)
                    
            print("Car was stopped")
        else:
            print("Car is stopped or No X-Box Controller found ..")
