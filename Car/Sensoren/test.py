import time

from hcrsr04 import UltraschallHCRSR04
from sensors import Sensors

sensoren = Sensors()
hcrsr04_sensor1 = UltraschallHCRSR04("UART2_RTS", "SPI2_SCK")

sensoren.add_sensor("HCRSR04", hcrsr04_sensor1)
HCR = sensoren.get_sensor("HCRSR04")

HCR.start()


while True:
    time.sleep(0.2)
    HCR.display_entfernung()
