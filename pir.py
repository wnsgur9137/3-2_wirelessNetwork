#!/usr/bin/python

import time
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb # influxDB

# print(GPIO.VERSION)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def interrupt_fired(channel):
    print("interrupt fired")
#     print(channel)
    a = 5
    data = [{
        'measurement': 'pir', # tableName
        'tags': {
            'VisionUni': '2410',
        },
        'fields': {
            'pir': a,
        }
    }]
    client = None
    
    try:
        # influxdb Connect
        # client = influxdb('localhost', 8086, 'root', 'root', 'a202044021')
        client = influxdb('localhost', 8086, 'root', 'root', 'pir')
    except Exception as e:
        print("Exception: " + str(e))
    if client is not None:
        try:
            client.write_points(data) # data
            print("client.write: " +str(data))
        except Exception as e:
            print("Exception write: " + str(e))
        finally:
            client.close() #influxdb 
    print(a)

GPIO.add_event_detect(4, GPIO.FALLING, callback=interrupt_fired)

while (True):
    time.sleep(1)
    # print("Timer Fired")
    a = 1
    data = [{
        'measurement': 'pir',
        'tags':{
            'VisionUni': '2410',
        },
        'fields': {
            'pir': a,
        }
    }]
    client = None
    try:
        # client = influxdb('localhost', 8086, 'root', 'root', 'a202044021')
        client = influxdb('localhost', 8086, 'root', 'root', 'pir')
    except Exception as e:
        print("Exception: " + str(e))
    if client is not None:
        try:
            client.write_points(data)
            # print("client.write: " +str(data))
        except Exception as e:
            print("Exception write: " + str(e))
        finally:
            client.close()
    print("running influxdb OK")
