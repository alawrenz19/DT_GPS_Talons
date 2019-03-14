import RPL
RPL.init()
import time
import GPS_2018

f_reverse = 1000
neutral = 1500
f_forward = 2000
#anglepersecond = 30

def DT_PWM_Establish():
	ServoR = int(raw_input("Pls input what pin you've inserted your right talon into > "))
	RPL.pinMode(ServoR, RPL.PWM)
	ServoL = int(raw_input("Pls input what pin you've inserted your left talon into > "))
	RPL.pinMode(ServoL, RPL.PWM)

DT_PWM_Establish()

# vec_angle(x1, y1, x2, y2) Brad: input the GPS coordinates into here. 
