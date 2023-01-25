from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Registertion_form
from django.shortcuts import redirect
from django.contrib import messages 
from django.contrib.auth import  authenticate
from django.contrib.auth import logout as authlogout
from django.contrib.auth import login  as authlogin
from django.contrib.auth.forms import AuthenticationForm ,PasswordResetForm
from django.contrib.auth.models import User
#  password reset 
# from django.db.models.query_utils import Q
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.template.loader import render_to_string
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse



def findex(req):
    return render(req,'index.html')
def register(req):
    form=Registertion_form()
    if req.method == 'POST':
        form=Registertion_form(req.POST)
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    return render(req,'register.html', {'form':form})
     
def userlogin(req):
     if req.user.is_authenticated:return redirect('index')
     form = AuthenticationForm()
     if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req,username=username,password=password) 
        if user is not None:
                authlogin(req,user)
                return redirect('index')
        else:
                messages.error(req,'not valid')
   
     con={'form':form}
     return render(req,"login.html",con)




# @login_required(login_url='userlogin')
def userlogout(req):
    authlogout(req)
    return redirect('/login')

def password_reset(req):
    user = req.user
    form = PasswordResetForm(user)
    return render(req, 'main/password/pass_reset.html', {'form': form})

# def password_reset_req(req):
# 	if req.method == "POST":
# 		password_reset_form = PasswordResetForm(req.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "main/password/password_reset_email.txt"
# 					c = {
# 					"email":user.email,
# 					'domain':'127.0.0.1:8000',
# 					'site_name': 'Website',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					"user": user,
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:
# 						return HttpResponse('Invalid header found.')
# 					return redirect ("/password_reset/done/")
# 	password_reset_form = PasswordResetForm()
# 	return render(req, template_name="main/password/pass_reset.html", context={"password_reset_form":password_reset_form})