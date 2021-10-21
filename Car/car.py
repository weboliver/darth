import RPi.GPIO as gpio


class Car:
    def __init__(self, name, motor, controller):
        self._name = name
        self._motorengine = motor
        self._controller = controller
        self._motorevents = {}
    
    def get_name(self):
        return self._name

    def get_controller(self):
        return self._controller

    def start(self):
        self.get_motorengine().start_motor()

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
        elif actionevent["action"] == "stopmotor":
            motor.stop()
        elif actionevent["action"] == "leftsteering":
            motor.leftsteering()
        elif actionevent["action"] == "rightsteering":
            motor.rightsteering()
        elif actionevent["action"] == "straightsteering":
            motor.straightsteering()
        else:
            motor.stop()

    def stop(self):
        self.get_motorengine().stop()

    def drive(self):
        controller = self.get_controller()
        if controller.get_device():
            while True:
                try:
                    actionevent = controller.get_action()
                    if actionevent:
                        self.handleevent(actionevent)
                except:
                    print("Ending Controller ..")
                    gpio.cleanup()
                    break
        else:
            print("No X-Box Controller found ..")

    def lockup(self):
        self.get_motorengine().stop_motor()
