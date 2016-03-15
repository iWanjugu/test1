from adlink.models import clerk_auth
class FetchUpdateData():
	def run(request_data,data):
		data['email']= FetchUpdateData.get_company_email(request_data,data)
		
		


	def get_company_email(request_data, data):
		form_data = data.get('form_data')
		company = form_data.get('company')
		email = clerk_auth.objects.filter(company=company).values('email')
		return email[0]

