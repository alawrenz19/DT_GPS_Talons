import RPL
RPL.init()
import time
from GPS_2018 import vec_angle.py

f_reverse = 1000
neutral = 1500
f_forward = 2000
#anglepersecond = 30

def DT_PWM_Establish():
	ServoR = int(raw_input("Pls input what pin you've inserted your right talon into > "))
	RPL.pinMode(ServoR, RPL.PWM)
	ServoL = int(raw_input("Pls input what pin you've inserted your left talon into > "))
	RPL.pinMode(ServoL, RPL.PWM)

#if __name__ == "__main__": use later
DT_PWM_Establish()

def DT_GPS_talons():
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0
def vec_trans_length(vec_length(x1,y1)):
  #robot goes 13.3 cm in 1 second
  	Length = abs(magnitude) * 15.24
  	Runtime = Length / 13.3
  	readtime = time.time()
 	while time.time() < (readtime + Runtime):
    		RPL.servoWrite(motorL, 2000)
		RPL.servoWrite(motorR, 1000)
  	if time.time() > (readtime + Runtime):
    		RPL.servoWrite(motorL, 0)
    		RPL.servoWrite(motorR, 0)





# vec_angle(x1, y1, x2, y2) Brad: input the GPS coordinates into here. 
