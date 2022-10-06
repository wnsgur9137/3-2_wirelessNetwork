import sys, serial, time
import requests, json
from influxdb import InfluxDBClient as influxdb

cmd = 'temp'
seri = serial.Serial('/dev/ttyACM0', 9600, timeout = 5)

seri.write(cmd.encode())



def interrupt_fired(dustDensity):
    data = [{
        'measurement': 'dustDenstiy',
        'tags': {
            'VisionUni': '2410',
        },
        'fields': {
            'dustDensity': dustDensity
        }
    }]
    client = None
    
    try:
        client = influxdb('localhost', 8086, 'root', 'root', 'dustDensity')
    except Exception as e:
        print("Exception: " + str(e))
    if client is not None:
        try:
            client.write_points(data)
            print("client.write: " + str(data))
        except Exception as e:
            print("Exception write: " + str(e))
        finally:
            client.close()
    print("Dust density: " + str(dustDensity))
    
while (True):
    if seri.in_waiting > 0:
        dustDensity = seri.readline()
        if dustDensity is not None:
            interrupt_fired(dustDensity)
        time.sleep(1)