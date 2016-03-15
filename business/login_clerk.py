from adlink.models import clerk_auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
class LoginClerk():
	def run(data):
		login_data= data.get('login_data')
		logindata= User(**login_data)
		username = logindata.username
		password = logindata.password
		check_details = authenticate(username = username, password=password)
		
		
