from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password']
class LoginForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username', 'password']

class ListingForm(forms.ModelForm):
  
	class Meta:
  		model = User
  		fields = ('__all__')
  		
  		# If specific fields only
  		# fields = ('artist', 'album_title',)
  		# exclude = ['album_logo']