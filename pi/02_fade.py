from gpiozero import PWMLED
from time import sleep

lamp_A = PWMLED(18)
lamp_B = PWMLED(23)
lamp_C = PWMLED(24)
lamp_D = PWMLED(25)

lamps = [lamp_A, lamp_B, lamp_C, lamp_D]

while True:
    for lamp in lamps:
        for brightness in range(0, 255):
            lamp.value(brightness / 255)
            sleep(0.01)
    for lamp in lamps:
        lamp.value(0)
    

