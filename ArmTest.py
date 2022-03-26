#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import serial
import time

ser=serial.Serial('COM10', 9600, timeout=5)

base=90
arm1=90
arm2=90
tilt=0

ON=True

while (ON==True):
    base=input("Enter Base Angle")    
    ser.write(base.encode())
    time.sleep(3)
    
    a1=input("Enter Arm 1 Angle")
    ser.write(a1.encode())
    time.sleep(3)
    
    a2=input("Enter Arm 2 Angle")
    ser.write(a2.encode())
    time.sleep(3)
    
    tilt=input("Enter Rotate angle")
    ser.write(tilt.encode())
    time.sleep(3)

        
    end=input("Enter another coorinate? 'Y/N' ")
    if (end.upper()!='Y'):
        ON=False;





# In[ ]:





# In[ ]:




