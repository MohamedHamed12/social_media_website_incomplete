from django import forms
from django.contrib.auth.models import User
from .models import Profile 
from django.contrib.auth.forms import UserCreationForm # very import
from django.contrib.auth.views import PasswordChangeView # very import
from django.urls import reverse_lazy
# class Registertion_form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
# class login_form(forms.ModelForm):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length = 50, widget=forms.PasswordInput)
    # username = forms.CharField(label = 'username')
    # password = forms.CharField(label = 'password', widget = forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = [ 'username', 'password']


# very import    
class Registertion_form(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email' ]
class PasswordResetForm(PasswordChangeView):
    pass
#     form_class=PasswordChangeView
#     success_url =reverse_lazy('home')