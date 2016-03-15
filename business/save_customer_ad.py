from django.http import HttpResponseRedirect, HttpResponse
from adlink.models import adpost
class SaveCustomerAd():
	def run(data):
		new_ad_data = data.get('new_ad_data')
		save_ad_data = adpost(**new_ad_data)
		new_ad_file = data.get('new_ad_file')
		save_image= adpost(**new_ad_file)
		title= save_ad_data.title
		description = save_ad_data.description
		location = save_ad_data.location
		company = save_ad_data.company
		paid_by=save_ad_data.paid_by
		image = save_image.image
		save =adpost(title=title, description=description, location=location, company=company, paid_by=paid_by, image=image)
		save.save()


		
        

		# save_ad_data.save()
		data['save_ad_data']= save_ad_data
		
		
		
		
