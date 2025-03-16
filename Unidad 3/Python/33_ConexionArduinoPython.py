# -> pip install pyserial
import serial as controlador

arduino = controlador.Serial("/dev/ttyACM0", baudrate=9600,timeout=1)