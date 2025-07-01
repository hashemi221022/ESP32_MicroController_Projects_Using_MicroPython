# import library
from network import WLAN, AF_IF, AUTH_WPA_WPA2_PSK
import time
# Set your ESP32's user and pass for access point
ssid = 'Milad'
password = 'Hashemi'

def config_access_point():
    """ configure an ESP32 as a Wi-Fi access point
    """
    # Access Point settings
    # Initialize the access point
    access_point = WLAN(AP_IF)
    access_point.active(False)  # Deactivate it first to ensure a clean configuration
    time.sleep(0.1)
    access_point.active(True) # activetion
    # Configure the access point
    access_point.config(essid=ssid, password=password, authmode=AUTH_WPA_WPA2_PSK)

    # Print the access point's configuration
    print('Access Point configured:')
    print('SSID:', ssid)
    print('Password:', password)
    print('IP address:', access_point.ifconfig()[0])

def run():
  """ run function
  """
  config_access_point()

run()



