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
	html_client = get_template('application/email_client.html')

	name = request.POST.get("name", "")
	year = request.POST.get("year", "")
	residence = request.POST.get("residence", "")
	method = request.POST.get("method", "")
	send_type = request.POST.get("type", "")
	icon = request.POST.get("icon", "")
	code = request.POST.get("code", "")

	c = context = Context({ 'name':name,
							'year':year,
							'residence':residence,
							'method':method,
							'type':send_type,
							'icon':icon,
							'code':code })

#Internal Mailing Handler 

	subject, from_email, to = 'New Signup', 'auto@lapel.co', 'concierge@lapel.co'
	html_content = htmly.render(c)
	msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

# Client Facing Handler

	subject, from_email, to = 'Hello from Lapel', 'Lapel@lapel.co', send_type
	html_client_content = html_client.render(c)
	msg = EmailMultiAlternatives(subject, html_client_content, from_email, [to])
	msg.attach_alternative(html_client_content, "text/html")
	msg.send()
	
	return render_to_response(template, RequestContext(request))
