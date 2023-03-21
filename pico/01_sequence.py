from machine import Pin
from utime import sleep

lamp_A = Pin(18, Pin.OUT)
lamp_B = Pin(19, Pin.OUT)
lamp_C = Pin(20, Pin.OUT)
lamp_D = Pin(21, Pin.OUT)

lamps = [lamp_A, lamp_B, lamp_C, lamp_D]

while True:
    for lamp in lamps:
        lamp.on()
        sleep(0.5)
    for lamp in lamps:
        lamp.off()
        sleep(0.5)
    
