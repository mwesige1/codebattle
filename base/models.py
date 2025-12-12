from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True,null=True)
    bio = models.TextField(null=True,blank=True)
    participart = models.BooleanField(default=True,null=True)


    # MAKE USERS TO SIGN IN WITH EMAIL NOT USERNAME
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['username']


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    name= models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    participants= models.ManyToManyField(User,blank=True,related_name='events')
    date= models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Submission(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)
    participant = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='submission')
    event = models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    details = models.TextField(blank=True,null=True)


    def __str__(self):
        return str(self.event)   + '----' +  str(self.participant)