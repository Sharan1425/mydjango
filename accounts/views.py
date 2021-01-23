from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from . forms import OrderForm,CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.

@unauthenticated_user
def registerpage(request):
     form = CreateUserForm()
     if request.method == 'POST':
          form = CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request,"Account was created sucessfully for    " + user)
               return redirect ('login_page')
     context= {'form':form}
     return render(request, 'accounts/register.html',context)

     
@unauthenticated_user
def login_page(request):
     if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request,username=username,password=password)
          if user is not None:
               login(request,user)
               return redirect('home')
          else:
               messages.info(request,"Username or Password incorrect")
     return render(request, 'accounts/login.html')


def logout_page(request):
     logout(request)
     return redirect ('login_page')


@login_required(login_url='login_page')
def home(request):
     customers = Customer.objects.all()
     orders = Order.objects.all()
     total_customers = customers.count()
     total_orders = orders.count()
     delivered = orders.filter(status='Delivered').count()
     pending = orders.filter(status='Pending').count()
     return render(request,'accounts/Dashboard.html',{'customers':customers,'orders':orders,
     'total_orders':total_orders,'delivered':delivered,'pending':pending})


@login_required(login_url='login_page')   
def products(request):
     products = Product.objects.all()
     return render(request,'accounts/products.html',{'products':products})


@login_required(login_url='login_page')
def customers(request, pk_test):
     customers = Customer.objects.get(id = pk_test)
     orders = customers.order_set.all()
     orders_count = orders.count()
     context = {'customers':customers,'orders':orders,'orders_count':orders_count}
     return render(request,'accounts/customers.html',context)


@login_required(login_url='login_page')
def createorder(request):
     form = OrderForm() # creating an object to the OrderForm #1st
     if request.method == "POST": #6th
          #print(request.POST)
          form = OrderForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     context = {'form':form}  #2nd
     return render(request,'accounts/orders_form.html',context) #3rd


@login_required(login_url='login_page')
def updateorder(request, pk):
     order = Order.objects.get(id=pk) # gets the specific order details
     #form = OrderForm(instance = order)# instance helps us when we click on update, exsisting order details will be reflected in the form fields
     if request.method == "POST":
          form = OrderForm(request.POST, instance=order)
          if form.is_valid():
               form.save()
               return redirect('/')
          else:
               return render(request,'accounts/orders_form.html',{'form':form})
     else:
          form = OrderForm(instance = order)
          return render(request,'accounts/orders_form.html',{'form':form})


@login_required(login_url='login_page')
def deleteorder(request, pk):
     order = Order.objects.get(id=pk) 
     print(order)
     #if request.method == "POST":
     order.delete()
     return redirect('/')
     #context = {'item':order}
     #return render(request,'accounts/delete.html',context)
