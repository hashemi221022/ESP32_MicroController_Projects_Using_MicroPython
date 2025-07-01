# import librart
from machine import Pin
import time
# set led pin
led_1 = Pin(19, Pin.OUT)
led_2 = Pin(18, Pin.OUT)
led_3 = Pin(17, Pin.OUT)
led_4 = Pin(16, Pin.OUT)
led_5 = Pin(15, Pin.OUT)
# list of led 
led_list = [led_1, led_2, led_3, led_4, led_5]
# loop for on and off 
while True:
    for led in led_list:        
        led.on() # light on
        time.sleep(1) # delay
        led.off() # light off
        time.sleep_ms(11) # delay