from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order

class OrderForm(ModelForm): # ModelForm class is used to create a form with that model fields

    class Meta:
        model = Order  # mention the model with you are going to use and also import that model
        fields = '__all__'   #__all__ says that create a form with the fields which that perticular model has
 
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']