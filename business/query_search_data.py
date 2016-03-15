from adlink.models import clerk_auth
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader, Context
class QuerySearchData():
	def run(data):
		search_data= data.get('search_data')
		query= search_data
		print(query)
		results=clerk_auth.objects.filter(company=query)
		print(results)
		template = loader.get_template('search.html')
		context= Context({'query':query, 'results':results})
		response = template.render(Context)
		return HttpResponseRedirect(context)
		print(query, results)

	
		
		
		
