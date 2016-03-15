class GetSearchData():
	def run(request_data, data):
		data['search_data'] = GetSearchData.get_search_data(request_data)
		print(request_data)	
	def get_search_data(request_data):
		search_data = {}
		search_data['company']= request_data.get('q')
		
		return search_data
