from django.conf import settings
from adlink.models import clerk_auth
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

class SendEmailConfirmation():
	def run(data):
		user_data = data.get('user_data')
		userdata= User(**user_data)
		password = (data.get('random_password'))
		
		# fromaddr = settings.EMAIL_HOST_USER
		# toaddr = userdata.email
		# msg = MIMEMultipart()
		# msg['From']= fromaddr
		# msg['To'] = toaddr
		# msg['Subject']="Adlink Email"
		# body = "SUCCESFUL REGISTRATION"
		# msg =attach(MIMEText(body, 'plain'))
		# server = smtplib.SMTP('smtp.gmail.com', 587)
		# server.starttls()
		# server.login(settings.EMAIL_HOST_USER, 'bensonngurumburu')
		# text = msg.as_string()
		# server.sendmail(fromaddr. toaddr, text)
		# server.quit()
		subject = "Adlink Registration Succesful"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, userdata.email
		text_content = 'Your adlink password. %s' % password
		html_content = "<p>This is your <strong>adlink</strong> password." "</p>"+str(password )
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
	
			
		
