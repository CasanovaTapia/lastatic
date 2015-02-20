from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from django.http import HttpResponse
from django.core.mail import EmailMessage
import mandrill
mandrill_client = mandrill.Mandrill('Rq5YwPyaFDhbaeCHuBI9eg')

def index(request):
	template = "application/index.html"

	context = Context()

	return render_to_response(template, RequestContext(request))

def send(request):

	template = "application/index.html"

	context = Context()

	name = request.POST.get("name", "")
	year = request.POST.get("year", "")
	residence = request.POST.get("residence", "")
	method = request.POST.get("method", "")
	send_type = request.POST.get("type", "")
	icon = request.POST.get("icon", "")

	email = EmailMessage(name, year, residence, method, send_type, icon to=['chason@lapel.co'])
	email.send()

	return render_to_response(template, RequestContext(request))
