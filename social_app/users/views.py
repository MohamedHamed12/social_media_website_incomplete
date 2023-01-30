from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registertion_form,UserUpdateForm ,ProfileUpdateForm ,login_form
from django.shortcuts import redirect
from django.contrib import messages 
from django.contrib.auth import  authenticate
from django.contrib.auth import logout as authlogout
from django.contrib.auth import login  as authlogin
from django.contrib.auth.forms import AuthenticationForm ,PasswordResetForm 
from django.contrib.auth.models import User
from .managers import CustomUserManager
#  password reset 
# from django.db.models.query_utils import Q
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.template.loader import render_to_string
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def profile(req):
    
    if req.method == 'POST':
        
        u_form=UserUpdateForm(req.POST,instance=req.user)
        p_form = ProfileUpdateForm(req.POST, req.FILES,instance=req.user.profile)
       
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            print('2done')
            
            return redirect('mainUrl')
    else:
        u_form=UserUpdateForm(instance=req.user)
        p_form = ProfileUpdateForm(instance=req.user.profile)
        con={'u_form':u_form,'p_form':p_form}
        return render(req, 'main/user/profile.html', con)


def main(req):
    return  render(req,'main.html', {})
def findex(req):
    return render(req,'index.html')
def register(req):
    if req.method == 'POST':
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        email=req.POST.get('email')
        password1=req.POST.get('password1')
        password2=req.POST.get('password2')
        
        if User.objects.filter(email=email).exists():
           return redirect('registerUrl')
        user = User.objects.create_user(email=email, password=password1,first_name=first_name,last_name=last_name)
        
        return redirect('loginUrl')
  
    return render(req,'register.html')

     
def userlogin(req):
  
     if req.method == 'POST':
      
        email=req.POST.get('email')
        password=req.POST.get('password1')
        print(email, password)
        user = authenticate(req,email=email,password=password) 
        if user is not None:
                authlogin(req,user)
                return redirect('mainUrl')
        messages.error(req,'not valid')
     
   
     con={}
     return render(req,"login.html",con)
 




# @login_required(login_url='userlogin')
def userlogout(req):
    authlogout(req)
    return redirect('/login')

def password_reset(req):
    user = req.user
    form = PasswordResetForm(user)
    return render(req, 'main/password/pass_reset.html', {'form': form})
