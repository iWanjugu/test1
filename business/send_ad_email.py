from adlink.models import clerk_auth
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
class SendAdEmail():
	def run (data):
		new_ad_data = data.get('new_ad_data')
		email = data.get('company_data').get('email')
		print(email)
		company= new_ad_data.get('company')
		
		subject ="Your Ad was added succesfully"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, email
		text_content = 'Your adlink ad has been added'
		html_content = "<p>This is your <strong>adlink</strong>"
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()










		
		
		
	
