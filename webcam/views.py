from django.shortcuts import render
from . import servo
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

def index(request):
	if request.method == 'POST':
		if(request.POST.get('left')):
			print("LEFT!")
			servo.turnServoDegree(5)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		elif(request.POST.get('right')):
			print("RIGHT!")
			servo.turnServoDegree(-5)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		else:
			print("ya done fcucked up")
	template = loader.get_template('webcam/test.html')
	return HttpResponse(template.render())
