from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from adlink.models import adpost


class SendEmailConfirmation():
	def run(data):
		new_ad_data  = data.get(' new_ad_data ')
		save_ad_data= adpost(**new_ad_data)
		
		
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
		subject = "Adlink ad was saved"
		subject, from_email, to = subject, settings.EMAIL_HOST_USER, userdata.email
		text_content = 'Your Ad was succesfully saved'
		html_content = "<p>Your ad was succesfully saved</p>"
		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html_content, "text/html")
		msg.send()
	
			
		
