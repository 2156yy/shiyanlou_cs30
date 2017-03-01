

import datetime
from django.http import Http404, HttpResponse

#def hello(request):
#	return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)


def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelte(hours=offset)
	htmk = "<html><body>In %s hour(s), it will be %s .</body><>/html" %(offsetdt)
	return HttpResponse(html)
