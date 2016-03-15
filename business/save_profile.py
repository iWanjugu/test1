from adlink.models import clerk_auth
from django.contrib.auth.models import User
class SaveProfile():
	def run(data):
		user_data = data.get('user_data')
		new_registrant = User(**user_data)   
		profile_data = data.get('profile_data')
		new_profile =  clerk_auth(**profile_data)
		company= new_profile.company
		phone = new_profile.phone
		print(company, phone)
		e=clerk_auth(company=company, phone=phone, email=new_registrant.email)
		# new_profile.save()
		e.save()
		data['new_profile'] = new_profile

	
		
