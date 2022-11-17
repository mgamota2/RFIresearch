import time

#Setup sequence
def setup(ser):
    print("Setting up robot \n")
    ser.write(b'G90\r\n')
    print('G90')

    time.sleep(1)

    print("Homing \n")
    ser.write(b'G28\r\n')
    print('G28')

    time.sleep(1)

    print("Finishing moves \n")
    ser.write(b'M400\r\n')
    print('M400')

    time.sleep(1)

    returnHome(ser)
    time.sleep(1)

#Move a distance on Z axis in mm
def moveZ(ser, distance):
    #Relative Mode
    ser.write(b'G91')
    print('G91')

    time.sleep(1)

    command = ('G91 G01 Z'+str(distance))
    print(command)

    ser.write(command.encode())

    time.sleep(1)

    if (distance>=0):
        print("Moving up ", distance, " on Z axis")
    else:
        print("Moving down ", distance, " on Z axis")
    

#Move a positive distance on X axis in mm
def moveX(ser, distance):
    #Relative Mode
    ser.write(b'G91')
    print('G91')
    
    command = ("G01 X"+str(distance))
    print(command)
    ser.write(command.encode())
    
    print("Moving ", distance, " on x axis")
    

#Move a distance on Y axis in mm
def moveY(ser, distance):
    #Relative Mode
    ser.write(b'G91')
    print('G91')
    
    command = ('G01 Y'+str(distance))
    print(command)
    ser.write(command)
    
    print("Moving ", distance, " on y axis")
    

#Return to home
def returnHome(ser):
    ser.write(b'G1 X0 Y0 Z0')
    
    print("Returning home")


#Move to absolute coordinates
def moveCoords(ser, x, y, z):
    command = ('G01 X'+str(x)+' Y'+str(y)+' Z'+str(z)+'\r\n')
    print(command)
    ser.write(command.encode())
    
    print("Moving to x=", x, ", y=", y, ", ", z, ", z=")
    
