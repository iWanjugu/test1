from adlink.models import clerk_auth
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
class SendAdUpdate():
	def run(data):
		email = data.get('email').get('email')
		print(email)
		
		subject ="Your Ad was Updated succesfully"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, email
		text_content = 'Your adlink ad has been Updated'
		html_content = "<p>Your adlink ad has been Updated</p>"
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		


		
