from adlink.models import clerk_auth
from django.contrib.auth.models import User
from django import forms
from .models import *






#-------------------------------------------------------------------------------------------------------------------- user auth
class authentication(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username',  'password',  'first_name','last_name')
		exclude = ['password',]
#-------------------------------------------------------------------------------------------------------------------capture additional info during registration
class additonaldetails(forms.ModelForm):

	class Meta:
		model = clerk_auth
		fields = ( 'email', 'company','phone',)

class offlinenewad(forms.ModelForm):

	class Meta:
		model= adpost
		# fields = {
        #     'title': forms.TextInput(attrs={'class': 'form_control'}),
		# 	'description': forms.TextInput(attrs={'class': 'form_control'}),
		# 	'location': forms.TextInput(attrs={'class': 'form_control'}),
		# 	'company': forms.TextInput(attrs={'class': 'form_control'}),
		# 	'paid_by': forms.TextInput(attrs={'class': 'form_control'}),
		# 	'image': forms.TextInput(attrs={'class': 'form_control'}),
        # }
		fields=('title', 'description', 'location','company', 'paid_by', 'image')

# class update_old_ad(forms.ModelForm):
# 	class Meta:
# 		model=adpost
# 		fields =('expiry_date', 'image')
