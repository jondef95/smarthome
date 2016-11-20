from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

def index(request):
	if request.method == 'POST':
		if(request.POST.get('left')):
			print("LEFT!")
			return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
		elif(request.POST.get('right')):
			print("RIGHT!")
			return HttpResponseRedirect('http://172.16.0.137:8081')
		else:
			print("ya done fcucked up")
	template = loader.get_template('webcam/test.html')
	return HttpResponse(template.render())