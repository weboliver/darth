#Bibliotheken
import threading
import time

import RPi.GPIO as gpio


class UltraschallHCRSR04:
    def __init__(self, Trigger, Echo, set_mode: bool = True):
        self._gpio = {}
        self._gpio["TRIGGER"] = Trigger
        self._gpio["ECHO"] = Echo
        if (set_mode):
            gpio.setmode(gpio.TEGRA_SOC)
        gpio.setwarnings(False)
        gpio.setup(self._gpio["TRIGGER"], gpio.OUT)
        gpio.setup(self._gpio["ECHO"], gpio.IN)
        self._entfernung_now = 0

    def _entfernung(self):
        while True:
            time.sleep(0.1)
            # Trig Low setzen (nach 0.01ms)
            gpio.output(self._gpio["TRIGGER"], True)
            time.sleep(0.0005)
            # Trig High setzen
            gpio.output(self._gpio["TRIGGER"], False)
            Startzeit = time.time()
            Endzeit = time.time()
            # Start/Stop Zeit ermitteln
            while gpio.input(self._gpio["ECHO"]) == 0:
                Startzeit = time.time()
        
            while gpio.input(self._gpio["ECHO"]) == 1:
                Endzeit = time.time()
        
            # Vergangene Zeit
            Zeitdifferenz = Endzeit - Startzeit

            # print(Zeitdifferenz, Endzeit, Startzeit)
            
            # Schallgeschwindigkeit (34300 cm/s) einbeziehen
            self._entfernung_now = round((Zeitdifferenz * 34300) / 2)
            if self._entfernung_now > 500:
                self._entfernung_now = 0

    def start(self):
        self.thread = threading.Thread(target=self._entfernung)
        self.thread.start()

    def display_entfernung(self):
        print(self._entfernung_now, " cm")

    def get_current_entfernung(self):
        return self._entfernung_now
