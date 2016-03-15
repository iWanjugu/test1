from django.shortcuts import render, render_to_response,get_object_or_404
from adlink.forms import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader, Context
from adlink.models import clerk_auth
from adlink.models import *
from adlink.forms import *
from django.shortcuts import render
from business import  generate_random_password
from business import get_details
from business import save_user
from business import save_event
from business import save_profile
from business import send_email_confirmation
from business import request_login
from business import login_clerk
from business import  results_clerk_login
from business import save_clerk_login_events
from business import get_search_data
from business import query_search_data
from business import save_search_transaction
from business import request_data_new_ad
from business import save_customer_ad
from business import  save_ad_event
from business import save_ad_image
from business import send_ad_email
from business import fetch_company_data
from business import http_response_register
from django.contrib import messages
from business import get_update_data
from business import save_ad_update
from business import update_ad_image
from business import fetch_update_data
from business import send_update_email


from django_mongoengine.forms.fields import DictField
from django_mongoengine.views import (
    CreateView, UpdateView,
    DeleteView, ListView,
    DetailView,
    EmbeddedDetailView,
)




#Create your views here.
#-------------------------------------------------------------------------------------------------------------------- home page

def home(request):
    data={}
    generate_random_password.GenerateRandomPassword.run(data)
    print(data)

    return render_to_response('home.html',{

      })

#-------------------------------------------------------------------------------------------------------------------- registration()
def register_customer(request):

    context = RequestContext(request)
    registered = False
    user_form = authentication(data=request.POST)
    profile_form = additonaldetails(data=request.POST)
    if request.method =='POST':
            data = {}
            get_details.GetDetails.run(request.POST, data)
            generate_random_password.GenerateRandomPassword.run(data)            
            save_user.SaveUser.run(data)
            save_profile.SaveProfile.run(data)
            send_email_confirmation.SendEmailConfirmation.run(data)
            save_event.SaveEvent.run(data)
            # http_response_register.HttpResponseRegister.run(data)
            #print(data)
            messages.success(request, "User Was registered successfully! An email confirmation email was sent!")
            return HttpResponseRedirect('/login')

        

  
    return render(request,
            'register.html',
            {'user_form':user_form, 'profile_form':profile_form, 'registered': registered},
            context_instance=RequestContext(request))


#--------------------------------------------------------------------------------------------------------------------clerk_registration()

def clerk_login(request):
    context = RequestContext(request)

    if request.method== 'POST':
        data = {}
        request_login.RequestLogin.run(request.POST, data)
        login_clerk.LoginClerk.run(data)
        results_clerk_login.ResultsClerkLogin.run( request, data)

        save_clerk_login_events.SaveCustomerLoginEvents.run(data)

        

    return render(request, 'login.html', 
                {},  context_instance=RequestContext(request))

#--------------------------------------------------------------------------------------------------------------------logout()

@login_required
def clerk_logout(request):
    logout(request)

    return HttpResponseRedirect('/login/')

   #----------------------------------------------------------------------------------------------------------------------search if a user exists 
def clerk_search(request):
    data = {}
    get_search_data.GetSearchData.run(request.GET, data)
    query_search_data.QuerySearchData.run(data)
    save_search_transaction.SaveSearchTransaction.run(data)
    





   #----------------------------------------------------------------------------------------------------------------------search if a user exists 
def  clerkAddAd(request):
    context = RequestContext(request)
    
    if request.method =='POST':
        
        ads_form = offlinenewad(request.POST, request.FILES)
        data = {}
        request_data_new_ad.RequestDataNewAd.run(request.POST, request.FILES, data)
        save_customer_ad.SaveCustomerAd.run(data)
        save_ad_image.SaveAdImage.run(data)
        fetch_company_data.FetchCompanyData.run(request,   data)
        send_ad_email.SendAdEmail.run(data)
        save_ad_event.SaveAdEvent.run(request, data)
        messages.success(request, "YEs")
        return HttpResponseRedirect('/login')
 
     
    else:

        ads_form = offlinenewad()
        print(ads_form)

        return render(request,
            'addofflinead.html',
            { 'ads_form':ads_form},
            context_instance=RequestContext(request))
 #----------------------------------------------------------------------------------------------------------------------Display ads

def DispalyCustomerAds(request):
        return render_to_response('clerk_ads.html',{'Ads': adpost.objects.all()})


#----------------------------------------------------------------------------------------------------------------------Display ads

def test(request, id=1):
    return render_to_response('id.html',{'a':adpost.objects.get(id=id) })


#----------------------------------------------------------------------------------------------------------------------Display ads


def update_ad(request, id):
    if id:
        instance = adpost.objects.get(id=id)
        form = offlinenewad(request.POST or None, instance=instance)
        if form.is_valid():
            data ={}
            get_update_data.GetUpdateData.run(request, request.FILES, data)
            save_ad_update.SaveAdUpdate.run(data, id)
            fetch_update_data.FetchUpdateData.run(request, data)
            send_update_email.SendAdUpdate.run(data)
            # update_ad_image.UpdateAdImage.run(data)
            # instance = form.save(commit=True)
            # instance.save()
            return HttpResponseRedirect('/login/')
        context = {
            "title": instance.title,
            "instance": instance,
            "form":form,
        }
        return render(request, "updatead.html", context)

# def update(request, slug):
    # return render_to_response('id.html',{'a':get_object_or_404(adpost, slug=slug)})

# def update_ad(request, id):
#     if id:
#         a = adpost.objects.get(id=id)
#         adpost.objects.filter(id=id).update(expiry_date="2017-03-31 10:20:38.461085+03")
#         # a.expiry_date = ""
        # adpost.expiry_date=a
        # a.save()
        # print(a.expiry_date)


        

        # return render_to_response('id.html',{'a':get_object_or_404(adpost, id=id)})
        # return render(request,'addofflinead.html',{ 'ads_form':ads_form},context_instance=RequestContext(request))