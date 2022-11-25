import time

speedX=10
speedY=10
speedZ=10

#Setup sequence
def setup(ser):
    
    ser.write(b'G90\r\n')
    print('G90')
    print("Setting up robot \n")

    ser.write(b'G28\r\n')
    print('G28')
    print("Homing \n")
    
    ser.write(b'M400\r\n')
    print('M400')
    print("Finishing moves \n")

    returnHome(ser)

#Current 
def updateCurr(x, y, z):
    global current
    current = [x, y, z]
    
def getCurr():
    return current

def isPossibleX(distance, maxTime):
    if ((distance/speedX)<time):
        print("Movement not possible in time \n")
        return False

def isPossibleY(distance, maxTime):
    if ((distance/speedY)<time):
        print("Movement not possible in time\n")
        return False

def isPossibleZ(distance, maxTime):
    if ((distance/speedZ)<time):
        print("Movement not possible in time\n")
        return False


#Move a distance on Z axis in mm
def moveZ(ser, distance):
    #Relative Mode
    ser.write(b'G91')
    print('G91')

    command = ('G91 G01 Z'+str(distance))
    print(command)

    ser.write(command.encode())
    updateCurr(current[0], current[1], current[2]+distance)

    if (distance>=0):
        print("Moving up ", distance, " on Z axis\n")
    else:
        print("Moving down ", distance, " on Z axis\n")
    

#Move a positive distance on X axis in mm
def moveX(ser, distance):
    #Relative Mode
    ser.write(b'G91')
    print('G91\n')
    
    command = ("G01 X"+str(distance))
    print(command + '\n')
    ser.write(command.encode())
    updateCurr(current[0]+distance, current[1], current[2])
    print("Moving ", distance, " on x axis\n")
    

#Move a distance on Y axis in mm
def moveY(ser, distance):
    #Relative Mode
    ser.write(b'G91')
    print('G91\n')
    
    command = ('G01 Y'+str(distance))
    print(command + '\n')
    ser.write(command)
    updateCurr(current[0], current[1]+distance, current[2])
    print("Moving ", distance, " on y axis\n")
    

#Return to home
def returnHome(ser):
    ser.write(b'G1 X0 Y0 Z0')
    updateCurr(0, 0, 0)
    print("Returning home\n")


#Move to absolute coordinates
def moveCoords(ser, x, y, z):
    command = ('G01 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\r\n')
    print(command)
    ser.write(command.encode())
    updateCurr(x, y, z)
    print("Moving to x=", x, ", y=", y, ", ", ", z=" ,z, "\n")
    
