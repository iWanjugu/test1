from adlink.models import search_customer_events
class SaveSearchTransaction():
	def run(data):
		search_event ={}
		search_event['title']= 'ClerkSearch'
		search_event ['search_data']= data.get('search_data')
		save = search_customer_events(**search_event)
		save.save()

