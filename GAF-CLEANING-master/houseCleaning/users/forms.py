from django import forms
from .models import Customer, Employee, Suppliers, create_property
from pages.models import ContactUs

class createCustomer(forms.ModelForm):
    class Meta:
        model=Customer
        fields=[ 
            'email',
            'fax'
        ]

class creationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    fax = forms.CharField(max_length=50)
    password1  =forms.CharField(max_length=50)
    password2 = forms.CharField(max_length=50)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class createUserForm(UserCreationForm):
    class Meta:
        model= User
        fields=['username','password1', 'password2']

class createEmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee 
        fields='__all__'
        exclude=['user']

class contact_us_form(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CreatePropertyForm(forms.ModelForm):
    class Meta:
        model = create_property
        fields = '__all__'
        exclude = ['customer']

class customerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'