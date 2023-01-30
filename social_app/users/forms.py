from django import forms
from django.contrib.auth.models import User
from .models import Profile ,CustomUser
from django.contrib.auth.forms import UserCreationForm # very import
from django.contrib.auth.views import PasswordChangeView # very import
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from django.contrib.auth.forms import AuthenticationForm  

from .models import CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()
class  UserUpdateForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['email','first_name', 'last_name']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model=Profile
        fields=['bio','image','data_birthday']

class Registertion_form(UserCreationForm):
    class Meta():

      model = User #this is the "YourCustomUser" that you imported at the top of the file  
      fields = ('first_name','last_name','email', 'password1', 'password2')

      widgets = {
            'first_name': forms.TextInput({'placeholder': 'first_name'}),
            'last_name': forms.TextInput({'placeholder': 'last_name'}),
            'email': forms.EmailInput({'placeholder': 'email'}),
            'password': forms.PasswordInput({'placeholder': 'password'}),
            'password2': forms.PasswordInput({'placeholder': 'confirm password'}),
        }

    def __init__(self, *args, **kwargs):
            super(Registertion_form, self).__init__(*args, **kwargs)
            self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password '})
            self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'})













class login_form(AuthenticationForm):
    email=forms.EmailField()
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput)

  
  
        

        
# class login_form(forms.ModelForm):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(max_length = 50, widget=forms.PasswordInput)
    # username = forms.CharField(label = 'username')
    # password = forms.CharField(label = 'password', widget = forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = [ 'username', 'password']


# very import    
 #etc etc, other fields you want displayed on the form)
#         def clean_email(self):
#             email = self.cleaned_data["email"]
#             if User.objects.filter(email=email).exists():
#                 raise ValidationError("An user with this email already exists!")
#             return email    
        # widgets = {
        #     'username': forms.TextInput({'placeholder': 'username'}),
        #     'email': forms.EmailInput({'placeholder': 'email'}),
        #     # 'password': forms.PasswordInput({'placeholder': 'password'}),
        #     # 'password2': forms.PasswordInput({'placeholder': 'confirm password'}),
        # }
        # def __init__(self, *args, **kwargs):
        #     super(Registertion_form, self).__init__(*args, **kwargs)
        #     self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'})
        #     self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})
# class PasswordResetForm(PasswordChangeView):
#     pass
#     form_class=PasswordChangeView
#     success_url =reverse_lazy('home')
# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = CustomUser
#         fields = ('email',)

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('email',)
