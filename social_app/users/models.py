from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser ,BaseUserManager
# from .managers import CustomUserManager


# src/users/model.py
from django.contrib.auth.base_user import BaseUserManager


from .managers import CustomUserManager

    
    
class CustomUser(AbstractUser):
    # email_verified = models.BooleanField(default=False)
    username = None
    email = models.EmailField( ('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    frinds = models.ManyToManyField(CustomUser, related_name='my_frinds', blank=True)
    following = models.ManyToManyField(CustomUser, related_name='my_following', blank=True)
    is_online = models.BooleanField(default=False)
    data_birthday = models.CharField(blank=True,max_length=150)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    image= models.ImageField(default='d.jpg',null=True)
    bio= models.CharField( default='',max_length=500,null=True)

    def __str__(self):
        return  f"{self.user.first_name} {self.user.last_name}"
    
STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')
)
class Realtion(models.Model):
    sender= models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="frind_sender")
    receiver= models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='frind_receiver')
    status= models.CharField(max_length=8,choices =STATUS_CHOICES)
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)

    def __str__(self):
            # return self.sender.user.username
            return f"{self.sender}-{self.receiver}-{self.status}"
 
            

    