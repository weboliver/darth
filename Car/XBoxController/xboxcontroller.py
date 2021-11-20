__all__ = ['XBoxController']

import threading
import time

import evdev
import ipywidgets as widgets
from IPython.display import display
from traitlets.traitlets import Bool

from .events import XBOXControllerEvents


class XBoxController:

    def __init__(self, debug: Bool = False):
        self._xbox_device = self.init_device()
        self._eventController = XBOXControllerEvents()
        self._info_box = widgets.Output(layout={'border': '1px solid black'})
        self._lastevent = ""
        self._debug = debug
        with self.get_info_box():
            print("X-Box Controller")

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

    def get_info_box(self):
        return self._info_box

    def display_output(self):
        display(self._info_box)

    def get_action(self):
        event = self.get_device().read_one()
        return self.translate_event(event)

    def get_lastevent(self):
        return self._lastevent

    def _run(self):
        while True:
            actionevent = self.get_action()
            if self._debug:
                if actionevent:
                    self._lastevent = actionevent
                    self._info_box.append_stdout(str(actionevent) + "\n")

    def run(self):
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def translate_event(self, event):
        result = None
        eventController = self.get_event_controller()
        if event is not None:
            if self._debug:
                if event:
                    self._info_box.append_stdout(str(event) + "\n")
            result = eventController.find_event(event)
        return result
