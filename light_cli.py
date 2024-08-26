import sys 
from time import sleep
import subprocess
import requests
import colorama

if sys.platform == "linux":
    result = subprocess.run(["iwconfig"], shell=True, capture_output=True, text=True)
    output = result.stdout

    if "Mode" in output:
        wireless_active = True
        print("Checking Wireless card is Enabled.....", end =" ")
        print(colorama.Fore.GREEN + " " + str(wireless_active))
    else:
        wireless_active = False
        print("Checking Wireless card is Enabled.....", end =" ")
        print(colorama.Fore.RED + " " + str(wireless_active))
    
    sleep(1)

    if 'ESSID:"Light"' in output:
        wireless_connect = True
        print(colorama.Fore.WHITE +"Checking Wireless card is Connected to Light AP.....", end =" ")
        print(colorama.Fore.GREEN + " " + str(wireless_connect))
    else:
        wireless_connect = False
        print(colorama.Fore.WHITE +"Checking Wireless card is Connected to Light AP.....", end =" ")
        print(colorama.Fore.RED + " " + str(wireless_connect))

    if sys.argv[1] == "off" and wireless_connect == True and wireless_active == True:
        response = requests.get('http://192.168.4.1/LEDON?')
    
    if sys.argv[1] == "on" and wireless_connect == True and wireless_active == True:
        response = requests.get('http://192.168.4.1/LEDOFF?')
