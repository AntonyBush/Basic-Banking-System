from django.db.models.fields import DecimalField
from django.forms import fields
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django import forms
from .models import Customer, Transfer
from django.contrib import messages
import re
# Create your views here.

all_customer_list=Customer.objects.all()
def home(request):
    return render(request,'home.html')
    
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','email','phone_no','account_no','ac_balance','pan_no']


def add_customer(request):
    if request.method=='POST':    
        c_form=CustomerForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.success(request,f'Successfully added Customer\'s Information')
            return redirect('customers')
    else:
        c_form=CustomerForm()

    context={
        'c_form':c_form,
    }
    return render(request,'customer_create.html',context)


def customer_list(request):
    customers = Customer.objects.all().order_by('account_no')
    return render(request,'customers.html',{'customers':customers})

def transfer_history(request):
    transfers = Transfer.objects.all().order_by('id')
    return render(request,'transfer.html',{'transfers':transfers})

def profile(request,cust_id):
    sender = Customer.objects.get(account_no=cust_id)
    if request.method == 'POST':
        receiver_id = request.POST['receiver']
        if request.POST['amount_transfer'] == '' or not re.match('[+-]?([0-9]*[.])?[0-9]+', request.POST['amount_transfer']):
            messages.error(request,'Please Enter Valid amount')
        else:
            amount = float(request.POST['amount_transfer'])

        if receiver_id == 'Select Customer':
            messages.error(request,'Please Select Customer')
        else:
            receiver = Customer.objects.get(account_no=receiver_id)
            if not amount > sender.ac_balance:
                seb=float(sender.ac_balance)
                reb=float(receiver.ac_balance)
                sender.ac_balance = (seb-amount)
                receiver.ac_balance = (reb+amount)
                sender.save()
                receiver.save()
                transfer_money = Transfer(debit_ac=sender.account_no,credit_ac=receiver.account_no,transfer_amount=amount)
                transfer_money.save()
                messages.success(request, 'Amount Transfered Successfuly')
                return redirect('profile',cust_id=sender.account_no)
                
            else:
                messages.error(request, 'Insufficient balance')
            
    return render(request,'profile.html',{'customer_list':all_customer_list, 'sender':sender})