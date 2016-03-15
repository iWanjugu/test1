from adlink.models import adpost
class GetUpdateData():
	def run(request_data,request_image, data):
		data['form_data']=GetUpdateData.get_form_data(request_data)
		data['updated_file']=GetUpdateData.get_new_image(request_image)
	
	def get_form_data(request_data):
		form_data ={}
		form_data['title']= request_data.POST.get('title')
		form_data['description']= request_data.POST.get('description')
		form_data['location']= request_data.POST.get('location')
		form_data['company']= request_data.POST.get('company')
		form_data['paid_by']= request_data.POST.get('paid_by')
		form_data['image']= request_data.POST.get('image')
		return form_data
	def get_new_image(request_image):
		updated_file = {}
		updated_file['image']= request_image.get('image')
		return updated_file
