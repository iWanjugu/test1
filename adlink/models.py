from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django_mongoengine import Document, EmbeddedDocument, DynamicDocument
from django_mongoengine import fields
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import permalink



#--------------------------------------------------------------------------------------------------------------------model for clerk login and customer registration

class clerk_auth(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(max_length=100, unique=False)
    email = models.CharField(max_length=100, unique=False)
    phone = models.CharField(max_length=100, unique=False)
    created_at= models.DateField(default= datetime.now, blank=False)
    updated_at = models.DateField(default=datetime.now, blank=False)

    def __unicode__(self):
        return self.user.username



#--------------------------------------------------------------------------------------------------------------------additional ad fields
class adpost(models.Model):
    title = models.CharField(max_length=250, unique=False)
    description = models.CharField(max_length=100, unique= False)
    location= models.CharField(max_length=100, unique=False)
    company = models.CharField(max_length=100, unique=False)
    paid_by = models.CharField(max_length=100, unique=False)
    image =models.FileField(upload_to="documents/%Y/%m/%d")
    created_at = models.DateField(default=datetime.now, blank=False)
    expiry_date=models.DateTimeField(default=timezone.now()+timedelta(days=30))
    # slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return '%s' %self.title
    # @permalink
    # def get_absolute_url(self):
    #     return('update', None, {'slug':self.slug})

#--------------------------------------------------------------------------------------------------------------------user  events
class user_events(DynamicDocument):
    title = fields.StringField(max_length=200, required=True)
    last_registration=fields.DateTimeField(default=datetime.now)

    #--------------------------------------------------------------------------------------------------------------------user  events
class login_customer_events(DynamicDocument):
    title = fields.StringField(max_length=200, required=True)
    last_login = fields.DateTimeField(default=datetime.now)

    #-------------------------------------------------------------------------------------------------------------------- ad fields
class search_customer_events(DynamicDocument):
    title = fields.StringField(max_length=200, required=True)
    search_done_on = fields.DateTimeField(default=datetime.now)

    #-------------------------------------------------------------------------------------------------------------------- ad fields

        #-------------------------------------------------------------------------------------------------------------------- ad fields
class save_ads_event(DynamicDocument):
    title = fields.StringField(max_length=200, required=True)
    status = fields.StringField(max_length=200, required=True)
    ad_posted_on = fields.DateTimeField(default=datetime.now)
    posted_by = fields.StringField(max_length=100, required=True)
    expiry_date=fields.DateTimeField(default=timezone.now()+timedelta(days=30))

    #-------------------------------------------------------------------------------------------------------------------- ad fields @permalink
