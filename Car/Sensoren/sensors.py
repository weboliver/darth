class Sensors:
    def __init__(self):
        self._sensoren = {}
    
    def add_sensor(self, name, sensor):
        self._sensoren[name] = sensor

    def get_sensor(self, name):
        return self._sensoren[name]

    def has_sensor(self, name):
        return name in self._sensoren
