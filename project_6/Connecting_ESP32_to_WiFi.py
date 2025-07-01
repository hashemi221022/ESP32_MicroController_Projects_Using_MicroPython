# import library
from network import WLAN, STA_IF
import time
# Enter your wifi user and pass
wifi_user = "Wokwi-GUEST"
wifi_pass = ""
# Creat station
station = WLAN(STA_IF)

def connect_to_wifi():
    try:
        if station.isconnected() == False:
            print("connecting to wifi...", end="")
            station.active(True) # active station
            station.connect(wifi_user, wifi_pass) # connect to wifi
            while not station.isconnected():
                print(".", end="")
                time.sleep(0.3)
            print("Connected!")
    except:
        print( "\nCould not connect to wifi", "\nPlease check wifi connection and try again!")

def run():
  """ run function
  """
  connect_to_wifi()
  print("Your request was done!")
run()

