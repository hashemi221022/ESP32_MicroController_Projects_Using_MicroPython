# Import linrary
from machine import Pin
from time import sleep
# number of Pins
button_pin = 34
led_pin = 23

# Set pins 
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
led = Pin(led_pin, Pin.OUT)

# led state
led_state = False

# toggle led state
def led_toggler():
  """ led state changer
  """
  global led_state
  led_state = not led_state
  led.value(led_state)


  
  
def interrupt_mode(pin):
  """intrrupt mode for on or off led 
  """
  if button.value() == False:
    led_toggler()
    
  
# run   
def run():
  """ run led toggler functoin in the loop
  """
  while True:
    sleep(0.2)
    button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt_mode)

run()