from machine import Pin, PWM
from utime import sleep

lamp_A = PWM(Pin(18, Pin.OUT))
lamp_B = PWM(Pin(19, Pin.OUT))
lamp_C = PWM(Pin(20, Pin.OUT))
lamp_D = PWM(Pin(21, Pin.OUT))

lamps = [lamp_A, lamp_B, lamp_C, lamp_D]

while True:
    for lamp in lamps:
        for brightness in range(0, 255):
            lamp.duty_u16(brightness * 256)
            sleep(0.01)
    for lamp in lamps:
        lamp.duty_u16(0)
    

