from adlink.models import clerk_auth
from django.contrib.auth.models import User

#TODO re enable save
class SaveUser():
	def run(data):
		user_data = data.get('user_data')
		new_registrant = User(**user_data)
		password = (data.get('random_password'))
		new_registrant.password = password
		new_registrant.set_password(password)
		new_registrant.save()
		data['new_registrant'] = new_registrant

		
		
