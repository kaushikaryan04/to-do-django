from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.utils import timezone
from .manager import UserManager
from main.settings import AUTH_USER_MODEL



class ToDo(models.Model):
    choice = (
        ('HI' , 'HIGH'),
        ('MID' , 'MEDIUM'),
        ('HIGH' , 'HIGH')
    )
    content = models.CharField(max_length=100 , blank=False , null = False)
    made_date = models.DateTimeField(default = timezone.now)
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=  5 ,choices = choice)
    user = models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE)

    def __str__(self):
        return self.content[0:10]
    

class User(AbstractBaseUser , PermissionsMixin ):
    username = models.CharField(max_length=20,null = False , blank = False , unique=True)
    email = models.EmailField(null = False , blank =False , unique = True)
    name = models.CharField(null = False , blank = False , max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default= False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' ,'name']
    objects = UserManager()

    def __str__(self):
        return self.name
