from django.db import models
from django.db.models.expressions import F
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
import uuid,string,random
from datetime import datetime,timedelta
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=25,default=None)
    email = models.EmailField(max_length=35)
    phone_no=PhoneNumberField(blank=True,max_length=15)
    account_no=models.IntegerField(primary_key=True)
    ac_balance=models.DecimalField(max_digits=9,decimal_places=2,default=None,null=True)
    pan_no=models.CharField(max_length=10,unique=True)
    def __str__(self):
        ac_no = str(self.account_no)
        return ac_no

class Transfer(models.Model):
    transfer_time = models.DateTimeField(auto_now_add=True)
    transfer_amount=models.DecimalField(max_digits=9,decimal_places=2,default=None,null=True)
    debit_ac= models.IntegerField()
    credit_ac=models.IntegerField()

    def __str__(self):
        tid = str(self.id)
        return 'Transfer ID '+tid