from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from django.http import HttpResponse

def index(request):
	template = "application/index.html"

	context = Context() 

	return render_to_response(template, RequestContext(request))
