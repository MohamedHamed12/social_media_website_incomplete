from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from users import views as users_views
from django.contrib.auth import views as auth_views # for reset password
urlpatterns = [
    path('',users_views.findex),
    path('register/',users_views.register,name='registerFun'),
    path('login/',users_views.userlogin,name='userlogin'),
    path('logout/',users_views.userlogout,name='userlogout'),
    # path('resetpassword/',users_views.resetpassword,name='resetpassword'),
    path('index/',users_views.findex,name='index'),
    path('reset_password/',auth_views.PasswordResetView.as_view( template_name='main/password/pass_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="main/password/password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="main/password/password_reset_complete.html"),name='password_reset_complete'),
    # path('password_reset/',users_views.password_reset,name='password_reset'),
    # path(
    #     'password_reset/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='main/password/pass_reset.html',
    #         success_url = '/'
    #     ),
    #     name='change_password'
    # ),
 


]






   # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'), name='password_reset_complete'),   
