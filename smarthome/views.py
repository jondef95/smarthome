from django.http import HttpResponse
from django.template import loader
def index(request):
	if request.method == 'GET':
		if(request.GET.get('left')):
			print("LEFT!")
		elif(request.GET.get('right')):
			print("RIGHT!")
		else:
			print("ya done fcucked up")
	template = loader.get_template('~/Documents/netapps/smarthome/templates/smarthome/test.html')
	return HttpResponse(template.render("", request))