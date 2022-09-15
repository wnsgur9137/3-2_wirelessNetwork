import time
import RPi.GPIO as GPIO
import requests, json
from influxdb import InfluxDBClient as influxdb
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.IN)

def interrupt_fired(humidity, temperature):
    print("interrupt fired")
    data = [{
        'measurement': 'dht',
        'tags': {
            'VisionUni': '2410',
        },
        'fields': {
            'humidity': humidity,
            'temperature': temperature,
        }
    }]
    client = None

    try:
        client = influxdb('localhost', 8086, 'root', 'root', 'dht')
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
    print("Humidity: " + str(humidity))
    print("Temperature: " + str(temperature))


humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

while (True):
    if humidity is not None and temperature is not None:
        interrupt_fired(humidity, temperature)

