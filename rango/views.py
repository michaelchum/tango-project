# Create your views here.

# Import HttpResponse object from django.http module
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

# Each views is an individual function, we only created one view called index
# Each view takes at least one argument, a HttpRequest object which is also from django.http module
# By convention, it is named request
# Each view must return a HttpResponse object
# A simple HttpResponse object takes as input a string representing the the content of the page sent to the client requesting the view

def index(request):
	# Request the context of the request
	# The context contains information such as the client's machine details for example.
	context = RequestContext(request)

	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage': "I am from the context"}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier
	# Note that the first parameter is the template we wish to use.
	return render_to_response('rango/index.html', context_dict, context)


def about(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "Rango says: Here is the about page."}
	return render_to_response('rango/about.html', context_dict, context)



