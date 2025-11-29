from time import sleep
from datetime import datetime
import time
import requests
import argparse
import schedule


parser = argparse.ArgumentParser(description='my simple light controller from cli', prog= 'light_cli.py')
parser.add_argument('-s', '--switch', type=str, help='Switch on/off', metavar= 'on , off , timer')
parser.add_argument('-c', '--clock', type=str, help='Set clock', metavar= '6:00')
parser.add_argument('-t', '--time', action="store_true", help='Show current time')

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

args = parser.parse_args()
sw = args.switch
time = args.time
clk = args.clock

if time == True:
    print("Current Time =", current_time)
       
if sw == "on":
    try:
        requests.get("http://192.168.4.1/on")
        print("")
        print("     ON LIGHT")
        print("")
    except:
        print("ERR: Connection Failed!")  
elif sw == "off":
    try:
        requests.get("http://192.168.4.1/off")
        print("")
        print("     OFF LIGHT")
        print("")
    except:
        print("ERR: Connection Failed!")
elif sw  == "timer":
    if clk == None:
        print("ERR: Clock not set!")
    else: 
        try:   
            requests.get("http://192.168.4.1/off")
            print("")
            print("     OFF LIGHT")
            print("     Current Time =", current_time)
            print("     Set Clock =", clk)
            print("")
            print("     Timer set!")
            print(" ")

            def sch():
                requests.get('http://192.168.4.1/on')
                sleep(5)
                requests.get('http://192.168.4.1/off')
                sleep(5)
                requests.get('http://192.168.4.1/on')
                print("Done !")
                
            schedule.every().day.at(clk).do(sch)
            
            while True:
                schedule.run_pending()
                sleep(1)
        except requests.exceptions.RequestException as err:
            print("ERR: Connection Failed!")
