import rospy
from Tkinter import *
from servo.Adafruit_PWM_Servo_Driver import PWM
from right_hand.msg import servoSet, servoCmd
Rpwm = PWM(0x41, 1)
Rpwm.setPWMFreq(30)
    
def sel(event):
   print scale.get()
   print E1.get()
   Rpwm.setPWM(int(E1.get()), 0, scale.get())

root = Tk()
L1 = Label(root, text="servo N: ")
L1.grid( row = 0, column=0)
var = StringVar(value='1')
E1 = Entry(root, textvariable=var)
E1.grid(row = 0, column=1)
scale = Scale( root, orient=HORIZONTAL, length=300, from_=100, to=300, command=sel)
scale.grid(row=1, column=0, columnspan=2)


root.mainloop()
