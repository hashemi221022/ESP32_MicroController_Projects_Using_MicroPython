# import library
from machine import ADC, Pin, PWM
from time import sleep

pot = ADC(Pin(34), atten=ADC.ATTN_11DB) # Set potentiometer
ledpin = Pin(23, Pin.OUT) # Set led pin
led = PWM(ledpin, freq= 1000, duty_u16=0) # Set led for use pwm

# Create the loop
while True:
    pot_value = pot.read_u16() # Read potentiometer value
    voltage = pot_value * (3.3/65535) # Voltage Range
    led.duty_u16(pot_value) # led light with potentiometer value
    sleep(1) # delay
    print(f"POTENTIOMETER : {pot_value} | VOLTAGE : {voltage}") # print potentiometer and voltage
