from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from datetime import datetime,timedelta

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=25,default=None)
    email = models.EmailField(max_length=35)
    phone_no=PhoneNumberField(blank=True,max_length=15)
    account_no=models.IntegerField(max_length=10,primary_key=True)
    ac_balance=models.DecimalField(decimal_places=2,default=None,null=True)
    pan_no=models.CharField(max_length=10,unique=True)

class Transfer(models.Model):
    transfer_id = models.UUIDField
    transfer_time = models.DateTimeField(auto_now_add=True)
    transfer_amount=models.DecimalField(decimal_places=2,default=None,null=True)
    sender_name= models.OneToOneField(Customer)