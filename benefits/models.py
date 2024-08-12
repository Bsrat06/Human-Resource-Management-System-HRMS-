from django.db import models
from datetime import date
class Benefit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    elligible = models.CharField(max_length=500, default='all')
    effective_date = models.DateField(default='07-11-2013')
    expiration_date = models.DateField()
    def __str__(self) :
        return f"{self.name}"
    class Meta :
        db_table = "Benefit"
class Enrollement(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.EmailField(default="123@gmail.com")
    ename = models.CharField(max_length=200,default="")
    cost = models.IntegerField(default=0)
    bid = models.IntegerField()
    name = models.CharField(max_length=200)
    Request = models.CharField(max_length=200,default="no request")
    expiration_date = models.DateField()
    Request_date = models.DateField(auto_now=True)
    enrollement_date = models.DateField(default="2000-11-11")
    state =  models.CharField(max_length=200,default='no request')
    type =  models.CharField(max_length=200,default="Other")
    detail = models.CharField(max_length=500)

class Notifications(models.Model):
    id = models.AutoField(primary_key=True)
    bid = models.IntegerField(default=0)
    user = models.EmailField(default="123@gmail.com" )
    ename = models.CharField(max_length=200,default="")
    Request = models.CharField(max_length=200,default="no request")
    state =  models.CharField(max_length=200)
    detail =  models.CharField(max_length=200)
    date = models.DateField()