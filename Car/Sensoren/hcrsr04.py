#Bibliotheken
import time

import RPi.GPIO as gpio

# Quelle: https://www.einplatinencomputer.com/raspberry-pi-ultraschallsensor-hc-sr04-ansteuern-entfernung-messen/

class UltraschallHCRSR04:
    def __init__(self, Trigger, Echo):
        self._gpio = {}
        self._gpio["TRIGGER"] = Trigger
        self._gpio["ECHO"] = Echo
        gpio.setmode(gpio.BOARD)
        gpio.setup(self._gpio["TRIGGER"], gpio.OUT)
        gpio.setup(self._gpio["ECHO"], gpio.IN)

    def entfernung(self):
        # Trig Low setzen (nach 0.01ms)
        gpio.output(self._gpio["TRIGGER"], False)
        time.sleep(0.0002)
        # Trig High setzen
        gpio.output(self._gpio["TRIGGER"], True)

        # Trig Low setzen (nach 0.01ms)
        time.sleep(0.0005)
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
        
        # Schallgeschwindigkeit (34300 cm/s) einbeziehen
        entfernung = (Zeitdifferenz * 34300) / 2
    
        return entfernung
