
from gcode import *
import serial
import time

PORT = 'COM14'
ser = serial.Serial(PORT, 250000)

time.sleep(1)
setup(ser)
time.sleep(5)
moveCoords(ser, 0, 0, 10)
time.sleep(5)
moveCoords(ser, 0, 20, 15)
ser.close()