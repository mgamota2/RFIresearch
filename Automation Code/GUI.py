from gcode import *
import serial
import time
import tkinter as tk

#Open serial
#PORT = 'COM14'
#ser = serial.Serial(PORT, 250000)

x=0
y=0
z=0

window = tk.Tk()
window.geometry('250x200')

tk.Label(window, text="X Coordinate").grid(row=2, column=2)
tk.Label(window, text="Y Coordinate").grid(row=3, column=2)
tk.Label(window, text="Z Coordinate").grid(row=4, column=2)

label = tk.Label(text="Control GUI", foreground = "white", background = "black").grid(row=0, column = 3)

entryX = tk.Entry()
entryX.grid(row=2, column=3)

x=entryX.get()

entryY = tk.Entry()
entryY.grid(row=3, column=3)

y=entryY.get()

entryZ = tk.Entry()
entryZ.grid(row=4, column=3)

z=entryZ.get()

move = tk.Button(text="Move")#command = moveCoords(ser, y, z)
move.grid(row=6, column=3)

window.mainloop()