from django.conf.urls import patterns, include, url
from adlink import views

from django_mongoengine import mongo_admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',


    url(r'^admin/', include(mongo_admin.site.urls)),
    url(r'^register/$', views. register_customer, name='register'),
    url(r'^login/$', views.clerk_login, name='clerk_login'),
    url(r'^logout/$', views.clerk_logout, name="logout"),
    url(r'^search/$', views.clerk_search, name='clerk_search'),
    url(r'^home/$', views.home, name='home'),
    url(r'^ClerkAd/$', views.clerkAddAd, name='OfflineNewAd'),
    url(r'^ads/$' ,views.DispalyCustomerAds, name='DispalyCustomerAds'),
    url(r'^update_ad/$' ,views.update_ad, name='update_ad'),
    # url(r'^(?P<slug>[\w\-]+)/$', views.update, name="update"),
    url(r'^get/(?P<id>\d+)/$', views.test, name="test"),
    url(r'^updateanAd/(?P<id>\d+)/$', views.update_ad, name="updateanAd"),


)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


