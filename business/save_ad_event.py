from adlink.models import save_ads_event
from django.contrib.auth.models import User
class SaveAdEvent():
        def run(request,data):
                ad_event = {}
                ad_event["category"]= "ClerkAds"
                ad_event["status"] = "Active"
                ad_event["posted_by"]= request.user.username
                # ad_event['new_ad_data']= data.get('new_ad_data')
                ad_event["title"]=data.get('new_ad_data').get('title')
                ad_event["description"] =data.get('new_ad_data').get('description')
                ad_event["location"] = data.get('new_ad_data').get('location')
                ad_event["company"] = data.get('new_ad_data').get('company')
                ad_event["paidby"] = data.get('new_ad_data').get('paid_by')
                
                
                #print(company, description, paidby, location, title)
                save = save_ads_event(**ad_event)
                save.save()
