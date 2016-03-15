class RequestLogin():
	def run(request_data, data):
		data['login_data']= RequestLogin.get_login_data(request_data)
		
	def get_login_data(request_data):
		login_data= {}
		login_data ['username'] = request_data.get('username')
		login_data  ['password']= request_data.get('password')
		return login_data
		
