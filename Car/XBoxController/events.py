class XBOXControllerEvents:
    def __init__(self):
        self._events = {}
        self.init_events()

    def add_event(self, name, typeofevent, code, type_id, value, action):
        eventkey = f"KEY_{code}_{value}"
        self._events[eventkey] = {}
        self._events[eventkey]["name"] = name
        self._events[eventkey]["typeofevent"] = typeofevent
        self._events[eventkey]["code"] = code
        self._events[eventkey]["type_id"] = type_id
        self._events[eventkey]["value"] = value
        self._events[eventkey]["action"] = action
        eventkeyalt = f"KEY_{code}_{type_id}_{value}"
        self._events[eventkeyalt] = {}
        self._events[eventkeyalt]["name"] = name
        self._events[eventkeyalt]["typeofevent"] = typeofevent
        self._events[eventkeyalt]["code"] = code
        self._events[eventkeyalt]["type_id"] = type_id
        self._events[eventkeyalt]["value"] = value
        self._events[eventkeyalt]["action"] = action


    def init_events(self):
        self.add_event("BTN_A", "BTN", 304, 1, 1, "")
        self.add_event("BTN_A", "BTN", 304, 1, 0, "")
        self.add_event("BTN_B", "BTN", 305, 1, 1, "")
        self.add_event("BTN_B", "BTN", 305, 1, 0, "")
        self.add_event("BTN_X", "BTN", 307, 1, 1, "")
        self.add_event("BTN_X", "BTN", 307, 1, 0, "")
        self.add_event("BTN_Y", "BTN", 308, 1, 1, "")
        self.add_event("BTN_Y", "BTN", 308, 1, 0, "")
        self.add_event("BTN_RT", "BTN", 311, 1, 1, "")
        self.add_event("BTN_RT", "BTN", 311, 1, 0, "")
        self.add_event("BTN_LT", "BTN", 310, 1, 1, "")
        self.add_event("BTN_LT", "BTN", 310, 1, 0, "")
        self.add_event("BTN_RB", "BTN", 9, 1, 1023, "rightslide")
        self.add_event("BTN_RB", "BTN", 9, 1, 0, "stop")
        self.add_event("BTN_LB", "BTN", 10, 1, 1023, "leftslide")
        self.add_event("BTN_LB", "BTN", 10, 1, 0, "stop")
        self.add_event("JOY_LEFT", "JOY_Y", 0, 1, 3, "")
        self.add_event("JOY_LEFT", "JOY_X", 1, 1, 3, "")
        self.add_event("JOY_RIGHT", "JOY_Y", 2, 1, 3, "")
        self.add_event("JOY_RIGHT", "JOY_X", 5, 1, 3, "")
        self.add_event("DPADUP", "BTN", 17, 3, -1, "forward")
        self.add_event("DPADUP", "BTN", 17, 3, 0, "stop")
        self.add_event("DPADLEFT", "BTN", 16, 3, -1, "leftsteering")
        self.add_event("DPADLEFT", "BTN", 16, 3, 0, "straightsteering")
        self.add_event("DPADRIGHT", "BTN", 16, 3, 1, "rightsteering")
        self.add_event("DPADRIGHT", "BTN", 16, 3, 0, "straightsteering")
        self.add_event("DPADDOWN", "BTN", 17, 3, 1, "backwards")
        self.add_event("DPADDOWN", "BTN", 17, 3, 0, "stop")
        self.add_event("START", "BTN", 315, 1, 1, "startmotor")
        self.add_event("START", "BTN", 315, 1, 0, "")
        self.add_event("STOP", "BTN", 158, 1, 1, "stopmotor")
        self.add_event("STOP", "BTN", 158, 1, 0, "")

    def get_events(self):
        return self._events

    def find_event(self, event):
        all_events = self.get_events()
        eventkey = f"KEY_{event.code}_{event.type}_{event.value}"
        if eventkey in all_events:
            return all_events[eventkey]
        eventkey = f"KEY_{event.code}_{event.value}"
        if eventkey in all_events:
            return all_events[eventkey]
        eventkey = f"KEY_{event.code}_{event.type}"
        if eventkey in all_events:
            return all_events[eventkey]
        return None


