# import library
from machine import Pin 
from time import sleep
# Set led pin
led = Pin(23, Pin.OUT)
# Set pir pin
pir = Pin(25, Pin.IN)

def detect_motion_to_on_led():
    """ on and off led with pir sensore
    """

    if pir.value() == True:
        led.on()
        print("motion was detected and the led turned on")
    else:
        led.off()
        print("No motion was detected and the led turned off.")
    sleep(2) # delay
    


def run():
    """run all function"""
    while True:
        detect_motion_to_on_led()

run()


