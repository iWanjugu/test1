class GetDetails():
	def run(request_data, data):
		print(request_data)
		data['user_data'] = GetDetails.get_user_data(request_data)
		data['profile_data']= GetDetails.get_profile_data(request_data)
	def get_user_data(request_data):
		user_data = {}
		user_data ['username'] = request_data.get('username')
		user_data ['email'] = request_data.get("email")
		user_data ['first_name'] = request_data.get("first_name")
		user_data ['last_name'] = request_data.get("last_name")
		return user_data

	def get_profile_data(request_data):
		profile_data = {}
		profile_data ['phone']= request_data.get('phone')
		profile_data ['company'] = request_data.get('company')	
		return profile_data
