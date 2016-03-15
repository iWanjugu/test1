from adlink.models import adpost
class SaveAdUpdate():
	def run(data, id):
		instance  = adpost.objects.get(id=id)
		form_data = data.get('form_data')
		updated_file= data.get('updated_file')
		save_image=adpost(**updated_file)
		save = adpost(**form_data)
		instance.title = save.title
		instance.description=save.description
		instance.location=save.location
		instance.company=save.company
		instance.paid_by=save.paid_by
		instance.image=save_image.image
		#print(instance.image,save.company, save_image.image)
		#instance.save()
		#save.save()
		data['save']= save
		
