import sys
import os 
from time import sleep
import time
import subprocess
import warnings
import requests
import colorama
import argparse
import schedule

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description='my simple light controller from cli', prog= 'light_cli.py')
parser.add_argument('-s', '--switch', type=str, help='Switch status', metavar= 'on / off')
parser.add_argument('-t', '--time', type=str, help='Time ON or OFF', metavar= '13:00')
parser.add_argument('-d', '--delay', type=float, help='Delay between on/off in seconds', metavar= '1')
parser.add_argument('-c', '--counter', type=int, help='Turn on/off counter', metavar= '1', default='5')

args = parser.parse_args()
sw = args.switch
ti = args.time
de = args.delay
count = args.counter

if sys.platform == "linux":
    result = subprocess.run(["iwconfig"], shell=True, capture_output=True, text=True)
    output = result.stdout

    if "Mode" in output:
        wireless_active = True
        print("Checking Wireless card is Enabled.....", end =" ")
        print(colorama.Fore.GREEN + " " + "Pass")
    else:
        wireless_active = False
        print("Checking Wireless card is Enabled.....", end =" ")
        print(colorama.Fore.RED + " " + "Fail")
    
    sleep(1)

    if 'ESSID:"Light"' in output:
        wireless_connect = True
        print(colorama.Fore.WHITE +"Checking Wireless card is Connected to Light AP.....", end =" ")
        print(colorama.Fore.GREEN + " " + "Pass")
    else:
        wireless_connect = False
        print(colorama.Fore.WHITE +"Checking Wireless card is Connected to Light AP.....", end =" ")
        print(colorama.Fore.RED + " " + "Fail")

    if sys.argv[1] == "off" and wireless_connect == True and wireless_active == True:
        response = requests.get('http://192.168.4.1/LEDON?')
    
    if sys.argv[1] == "on" and wireless_connect == True and wireless_active == True:
        response = requests.get('http://192.168.4.1/LEDOFF?')


if sys.platform == "win32":

    t = subprocess.run(["powershell", "-command", "(get-netconnectionProfile).Name"], shell=True, capture_output=True, text=True)
    result = subprocess.run(["ipconfig", "/all"], shell=True, capture_output=True, text=True)    
    output = result.stdout    

    if "Light" in t.stdout:
        if "Wireless LAN adapter Wi-Fi:" in output:
            wireless_active = True
        else:
            wireless_active = False
            

        if '192.168.4.1' in output:
            wireless_connect = True
        else:
            wireless_connect = False
            
        if sw == "on" and wireless_connect == True and wireless_active == True:
            response = requests.get('http://192.168.4.1/LEDOFF?')

        if sw == "off" and wireless_connect == True and wireless_active == True:
            response = requests.get('http://192.168.4.1/LEDON?')

        if sw == "star":
            for i in range(0, count):
                i += 1
                print("count ",i)
                if de:
                    sleep(de)
                else:
                    sleep(1)
                res = requests.get('http://192.168.4.1/LEDON?')
                if de:
                    sleep(de)
                else:
                    sleep(1)
                res = requests.get('http://192.168.4.1/LEDOFF?')
        
        if sw == "timer":
            print("Time set to:", ti)
            def sch():
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                print("Done !")
                
            schedule.every().day.at(ti).do(sch)
            
            while True:
                schedule.run_pending()
                time.sleep(1)
                
    else: 
        os.system('powershell.exe netsh interface set interface “Wi-Fi” Enable')
        os.system('powershell Set-NetAdapterAdvancedProperty -Name "Wi-Fi" -AllProperties -RegistryKeyword "SoftwareRadioOff" -RegistryValue "0"')
        sleep(10)
        print("Connecting to Light AP.....")
        os.system('netsh wlan connect Light')
        sleep(10)
        result = subprocess.run(["ipconfig", "/all"], shell=True, capture_output=True, text=True)    
        output = result.stdout
    
        if "Wireless LAN adapter Wi-Fi:" in output:
            wireless_active = True
            print(colorama.Fore.WHITE + "Checking Wireless card is Enabled.....", end =" ")
            print(colorama.Fore.GREEN + " " + "Pass")
        else:
            wireless_active = False
            print(colorama.Fore.WHITE + "Checking Wireless card is Enabled.....", end =" ")
            print(colorama.Fore.RED + " " + "Fail")

        if '192.168.4.1' in output:
            wireless_connect = True
            print(colorama.Fore.WHITE +"Checking Wireless card is Connected to Light AP.....", end =" ")
            print(colorama.Fore.GREEN + " " + "Pass")
        else:
            wireless_connect = False
            print(colorama.Fore.WHITE +"Checking Wireless card is Connected to Light AP.....", end =" ")
            print(colorama.Fore.RED + " " + "Fail")

        if sw == "on" and wireless_connect == True and wireless_active == True:
            response = requests.get('http://192.168.4.1/LEDOFF?')

        if sw == "off" and wireless_connect == True and wireless_active == True:
            response = requests.get('http://192.168.4.1/LEDON?')
        
        if sw == "star":
            for i in range(0, count):
                i += 1
                print("count ",i)
                if de:
                    sleep(de)
                else:
                    sleep(1)
                res = requests.get('http://192.168.4.1/LEDON?')
                if de:
                    sleep(de)
                else:
                    sleep(1)
                res = requests.get('http://192.168.4.1/LEDOFF?')
        
        if sw == "timer":
            print("Time set to:", ti)
            def sch():
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDON?')
                sleep(10)
                res = requests.get('http://192.168.4.1/LEDOFF?')
                print("Done !")
                
            schedule.every().day.at(ti).do(sch)
            
            while True:
                schedule.run_pending()
                time.sleep(1)
