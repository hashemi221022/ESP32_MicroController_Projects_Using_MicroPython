
# import library
from machine import Pin
import time
# led pin mode
led = Pin(22, Pin.OUT)
# button pin mode
button = Pin(32, Pin.IN)

# loop for flasher with button
while True: # flash light with button on
    if button.value() == True:
        led.value(1)
        time.sleep(1)
        led.value(0)
        time.sleep(2)
    else: # led off when button off
        led.off()
