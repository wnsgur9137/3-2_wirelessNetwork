import serial

port = '/dev/ttyACM0'
brate = 9600

seri = serial.Serial(port, baudrate = brate, timeout = None)
print(seri.name)

while True:
    if seri.in_waiting != 0:
        content = seri.readline()
        print(content.decode())
        a = 0
