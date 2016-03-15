from adlink.models import login_customer_events
class SaveCustomerLoginEvents():
	def run(data):
		login_event = {}
		login_event['title']= "CustomerLogins"
		login_event['login_data']= data.get('login_data')
		save = login_customer_events(**login_event)
		save.save()
		

		
