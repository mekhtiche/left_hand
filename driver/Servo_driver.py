#!/usr/bin/env python
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import rospy
from left_hand.msg import servoSet
from servo.Adafruit_PWM_Servo_Driver import PWM
print "LEFT SERVO_DRIVER successful import"

Lpwm = PWM(0x41, 1)

Lpwm.setPWMFreq(30)




def doIt(Lcmd):
    
    Lpwm.setPWM(1, 0, Lcmd[0])
    Lpwm.setPWM(2, 0, Lcmd[1])
    Lpwm.setPWM(3, 0, Lcmd[2])
    Lpwm.setPWM(4, 0, Lcmd[3])
    Lpwm.setPWM(5, 0, Lcmd[4])
    Lpwm.setPWM(6, 0, Lcmd[5])
    Lpwm.setPWM(7, 0, Lcmd[6])
    Lpwm.setPWM(8, 0, Lcmd[7])
    Lpwm.setPWM(9, 0, Lcmd[8])



def callback(data):
    print data
    #doIt(data.left_cmd)





if __name__ == '__main__':

    rospy.init_node('Left_hand_driver', anonymous=True)
    rospy.Subscriber('servo/Lcmd', servoSet, callback=callback)
    print 'LEFT SERVO_DRIVER publishers & subscribers successful Initial'
    rospy.spin()
