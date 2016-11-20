import time, threading
import RPi.GPIO as GPIO
import numpy as np

def main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	p = GPIO.PWM(12, 50)

	p.start(1.6)
	if True:
		try:
			steps = np.arange(1.6, 11, 0.052)
			for i in steps:
				p.ChangeDutyCycle(i)
				time.sleep(0.1)
		except KeyboardInterrupt:
			pass

	p.stop()
	GPIO.cleanup()

def turnServoDegree(degree):
	f = open('servo_pos.txt', 'rw')
	curr_degree = int(f.readline())
	next_degree = curr_degree + degree 
	if (next_degree > 180)
		next_degree = 180
	next_pos = (next_degree * 0.052) + 1.6
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	p = GPIO.PWM(12, 50)

	p.start(curr_pos)
	time.sleep(1)
	p.stop()
	GPIO.cleanup()

	f.write(str(next_degree))
	f.close()
