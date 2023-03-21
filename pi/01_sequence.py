from gpiozero import LED
from time import sleep

lamp_A = LED(18)
lamp_B = LED(23)
lamp_C = LED(24)
lamp_D = LED(25)

lamps = [lamp_A, lamp_B, lamp_C, lamp_D]

while True:
    for lamp in lamps:
        lamp.on()
        sleep(0.5)
    for lamp in lamps:
        lamp.off()
        sleep(0.5)
    
