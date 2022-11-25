
from gcode import *
import serial
import time

#Open serial
PORT = 'COM14'
ser = serial.Serial(PORT, 250000)

#Setup
setup(ser)
time.sleep(1)

#Test absolute movement
moveCoords(ser, 0, 0, 10)
time.sleep(3)
moveCoords(ser, 0, 20, 15)
time.sleep(3)

#Test relative Z movement
moveZ(ser, 10)
print(getCurr)
time.sleep(2)
moveZ(ser, -5)
print(getCurr)
time.sleep(2)

#Test relative Y movement
moveY(ser, 5)
print(getCurr)
time.sleep(2)
moveY(ser, -5)
print(getCurr)
time.sleep(2)

#Test if Y movement possible
if (isPossibleY(10, 3)):
    moveY(ser, 10)
    time.sleep(2)
else:
    print("Movement is impossible")


#Close
returnHome(ser)
ser.close()