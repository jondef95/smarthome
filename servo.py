import time, threading
import RPi.GPIO as GPIO
import numpy as np

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
