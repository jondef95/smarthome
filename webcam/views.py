from django.shortcuts import render_to_response
from . import servo
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
import os
def index(request):
	if request.method == 'POST':
		if(request.POST.get('left')):
			print("LEFT!")
			servo.turnServoDegree(15)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		elif(request.POST.get('right')):
			print("RIGHT!")
			servo.turnServoDegree(-15)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		else:
			print("ya done fcucked up")
	template = loader.get_template('webcam/camera.html')
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'servo_pos.txt')
	f = open(file_path, 'r')
	curr_degree = int(f.readline())
	f.close()
	return render_to_response('webcam/camera.html', {'degree':str(curr_degree)})
