# import library
from network import WLAN, STA_IF
from urequests import get
import json
import time
# Enter your wifi user and pass
wifi_user = "Wokwi-GUEST"
wifi_pass = ""
# Api url
api_url = "http://api.open-meteo.com/v1/forecast?latitude=32&longitude=53&hourly=temperature_2m&start_date=2025-06-24&end_date=2025-07-08"

def connect_to_wifi():
    try:
        station = WLAN(STA_IF) # create wlan abj
        if station.isconnected() == False:
            print("\n\nconnecting to wifi", end="")
            station.active(True) # active station
            station.connect(wifi_user, wifi_pass) #connect to wifi
            while not station.isconnected():
                print(".", end="")
                time.sleep(0.3)
            print("Connected!")
            print(f"IP address: {station.ifconfig()[0]}\n\n")
    except:
        print( "\nCould not connect to wifi", "\nPlease check wifi connection and try again!")


def get_temperature():
    try:
        response = get(api_url) # Requests to API server
        # Receive info from API And show that.
        if response.status_code == 200:
            data = response.json() # json format file
            temperature = data['hourly']['temperature_2m'][0] # Receive tepperature 
            print(f"Temperature is {temperature} celsius degree.\n\n")
        else:
            print(f"No Response \n Error {response.status_code}")
    except Exception as ex:
        print('Error:', ex)


def run():
  """ run function
  """
  # connect to wifi
  connect_to_wifi() 
  # Get info from API and show results
  get_temperature()
run()















