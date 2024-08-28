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

if sw == "on":
    response = requests.get('http://192.168.4.1/LEDOFF?')

if sw == "off":
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
