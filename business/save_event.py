from adlink.models import user_events
class SaveEvent():
	def run(data):
		event = {}
		event ['title']= 'ClerkSaveUser'
		#event ['user_data']= data.get('user_data')
		#event ['profile_data']= data.get('profile_data')
		event['username'] = data.get('user_data').get('username')
		event['first_name']=data.get('user_data').get('first_name')
		event['last_name']=data.get('user_data').get('last_name')
		event['email'] = data.get('user_data').get('email')
		event['phone'] = data.get('profile_data').get('phone')
		event['company'] = data.get('profile_data').get('company')
		#print(username, first_name, last_name, email, phone, company)
		m = user_events(**event)
		m.save()	
		
		

		
		
