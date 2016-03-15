from adlink.models import clerk_auth
class FetchCompanyData():
	def run(request_data,data):
		print(request_data)
		data['company_data']=FetchCompanyData.get_company_email(request_data,data)
	

	def get_company_email(request_data, data):
		new_ad_data = data.get('new_ad_data')
		company = new_ad_data.get('company')
		company_email = clerk_auth.objects.filter(company=company).values('email')
		return company_email[0]
