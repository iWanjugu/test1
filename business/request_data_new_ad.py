class RequestDataNewAd():
	def run(request_data,request_files,data):
		
		data['new_ad_data']=RequestDataNewAd.get_data(request_data)		
		data['new_ad_file']=RequestDataNewAd.get_image(request_files)

	def get_data(request_data):
		new_ad_data ={}
		new_ad_data ['title']= request_data.get('title')
		new_ad_data['description']= request_data.get('description')
		new_ad_data['location']= request_data.get('location')
		new_ad_data['company']= request_data.get('company')
		new_ad_data['paid_by']= request_data.get('paid_by')
		return new_ad_data
	def get_image(request_files):
		new_ad_file ={}
		new_ad_file['image']= request_files.get('image')
		return new_ad_file
