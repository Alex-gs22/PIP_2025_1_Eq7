import serial
import time

# /dev/ttyUSB0, /dev/ttyACM1
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

time.sleep(2)

while True:
    accion = input("Ingresa 3 digitos que contengan 0 y 1 unicamente: ")

    arduino.write((accion + "\n").encode())

    time.sleep(0.1)
