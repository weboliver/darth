import evdev

from XBoxController.events import XBOXControllerEvents


class XBoxController:
    def __init__(self):
        self._xbox_device = self.init_device()
        self._eventController = XBOXControllerEvents()

    def init_device(self):
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
            if (device.name.__contains__('box') is True) and (device.name.__contains__('Cons') is False):
                return device
        return None

    def get_event_controller(self):
        return self._eventController

    def get_device(self):
        if self._xbox_device is None:
            self._xbox_device = self.init_device()
            if self._xbox_device is None:
                raise RuntimeError("Error: No X-Box device found ...")
        return self._xbox_device

    def get_action(self):
        event = self.get_device().read_one()
        return self.translate_event(event)

    def translate_event(self, event):
        result = None
        eventController = self.get_event_controller()
        if event is not None:
            result = eventController.find_event(event)
        return result
