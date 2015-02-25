from django.shortcuts import render, render_to_response
from django.template import Context,RequestContext
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def index(request):
	template = "application/index.html"

	context = Context()

	return render_to_response(template, RequestContext(request))

def send(request):

	template = "application/index.html"

	htmly = get_template('application/email.html')

	name = request.POST.get("name", "")
	year = request.POST.get("year", "")
	residence = request.POST.get("residence", "")
	method = request.POST.get("method", "")
	send_type = request.POST.get("type", "")
	icon = request.POST.get("icon", "")

	c = context = Context({ 'name':name,
							'year':year,
							'residence':residence,
							'method':method,
							'type':send_type,
							'icon':icon })

	subject, from_email, to = 'New Signup', 'auto@lapel.co', 'jeffrey@lapel.co'
	html_content = htmly.render(c)
	msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

	return render_to_response(template, RequestContext(request))
