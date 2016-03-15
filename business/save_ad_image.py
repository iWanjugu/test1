from adlink.models import adpost
class SaveAdImage():
	def run(data):
		new_ad_file = data.get('new_ad_file')
		save_image= adpost(**new_ad_file)
		save_image.save()
		data['save_image']= save_image

