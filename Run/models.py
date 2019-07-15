from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
    conferences=models.ManyToManyField('Conferences')
    webinars=models.ManyToManyField('Webinars')
    collab=models.ManyToManyField('Collab')
    COI=models.ManyToManyField('Certify')
    labo=models.ManyToManyField('Industry')
    research1=models.ManyToManyField('Research1')
    research2=models.ManyToManyField('Research2')
   # name=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Conferences(models.Model):
    profile1=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pro',null=True)
    activity=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    state=models.CharField(max_length=1000)
    sponsor=models.CharField(max_length=1000)
    organizer=models.CharField(max_length=1000)
    #numb=models.IntegerField(default=0)
    #remarks=models.TextField()
    #acc_date=models.DateField(auto_now=False)

    def __str__(self):
        return (str(self.activity))

class Webinars(models.Model):
    profile1=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pro1',null=True)
    activity=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    speaker=models.CharField(max_length=1000)
    number=models.CharField(max_length=1000)
    remark=models.TextField(default='')

    def __str__(self):
        return str(self.activity)

class Collab(models.Model):

    profile1=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pro2',null=True)
    activity=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    period=models.CharField(max_length=1000)
    coordinator=models.CharField(max_length=1000)
    remark=models.TextField(default='')

    def __str__(self):
        return str(self.activity)

class Certify(models.Model):
    profile1=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pro3',null=True)
    activity=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    invest=models.CharField(max_length=1000)
    remark=models.TextField(default='')

    def __str__(self):
        return str(self.activity)

class Industry(models.Model):
    profile1=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pro4',null=True)
    activity=models.CharField(max_length=1000)
    lab=models.CharField(max_length=1000,default='')
    grant=models.CharField(max_length=1000,default='')
    year=models.CharField(max_length=1000,default='')
    scope=models.TextField(default='')

    def __str__(self):
        return str(self.activity)

class Research1(models.Model):
    profile1=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pro5',null=True)
    head=models.CharField(max_length=1000,default='')
    title=models.CharField(max_length=1000)
    authority=models.CharField(max_length=1000,default='')
    period=models.CharField(max_length=1000,default='')
    grant=models.CharField(max_length=1000,default='')
    order=models.CharField(max_length=1000,default='')

    def __str__(self):
        return str(self.title)


class Research2(models.Model):
    profile1=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='pro6',null=True)
    head=models.CharField(max_length=1000,default='')
    title=models.CharField(max_length=1000)
    authority=models.CharField(max_length=1000,default='')
    period=models.CharField(max_length=1000,default='')
    grant=models.CharField(max_length=1000,default='')
    order=models.CharField(max_length=1000,default='')

    def __str__(self):
        return str(self.title)



"""
 class Lab(models.Model):
      profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
      name=models.CharField(max_length=1000)"""
