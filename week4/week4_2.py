import sys, serial, time

cmd = 'temp'
seri = serial.Serial('/dev/ttyACM0', 9600, timeout = 5)
print(seri)

seri.write(cmd.encode())

while (True):
    if seri.in_waiting > 0:
        content = seri.readline()
        print(content[:].decode())
        time.sleep(1)