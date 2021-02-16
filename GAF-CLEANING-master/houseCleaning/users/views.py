from django.shortcuts import render, redirect
from .forms import createCustomer,createUserForm, creationForm, createEmployeeForm, contact_us_form

from .models import Customer, Employee2
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from pages.models import ContactUs



# Create your views here.

def datap(request):
    return render(request, "datapolicy.html")

def envip(request):
    return render(request, "environmentalpolicy.html")

def privatep(request):
    return render(request, "privacypolicy.html")

def socialp(request):
    return render(request, "socialmediapolicy.html")

def aboutus(request):
    return render(request, "about.html")

from icecream import ic
def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactUs.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return redirect('home')
        
    
    return render(request, "contact.html")

def carehomes(request):
    return render(request, "carehomes.html")

def carpets(request):
    return render(request, "carpets.html")

def events(request):
    return render(request, "events.html")

def pbandc(request):
    return render(request, "pbandc.html")

def pwss(request):
    return render(request, "pwss.html")

def pubsandclubs(request):
    return render(request, "pubsandclubs.html")

def retail(request):
    return render(request, "retail.html")

def schoolcu(request):
    return render(request, "schoolcu.html")

def sportsleisure(request):
    return render(request, "sportsleisure.html")

def window(request):
    return render(request, "window.html")

def vacateproperty(request):
    return render(request, "vacateproperty.html")

     
def SignUp(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    else:
        form = creationForm(request.POST)
        context = {
            "form":form
        }


        # TODO: Expcetions
        if form.is_valid():
            USER = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1'),
                    email=form.cleaned_data.get('email')
                )
            Customer.objects.create(
                name = form.cleaned_data.get('username'),
                email = form.cleaned_data.get('email'),
                fax = form.cleaned_data.get('fax'),
                user = USER
            )
            group = Group.objects.get(name='Customer')
            USER.groups.add(group)

            print("USER CREATED")
            return redirect('login')
            
        return render(request, "signup.html", context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print("----USERL ", user)
            if user is not None:
                login(request, user)
                return redirect('home')
            # else:
            #     messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, "index.html", context)

def Logout(request):
    logout(request)
    return redirect('home')

login_required(login_url='home')
def addEmployees(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        form = createEmployeeForm(request.POST)
        form2 = createUserForm(request.POST)
        print(form2.is_valid())
        print(form.is_valid)
        if form2.is_valid() and form.is_valid:
            user = form2.save()
            employee = form.save()
            group = Group.objects.get(name='Employees')
            user.groups.add(group)
            employee.user = user
            employee.save()
            emp2 = Employee2.objects.create(
                customer = employee
            )
            emp2.save()
            return redirect("dashboard")


        context = {
            "form":form,
            "form2":form2
        }
        return render(request, "AddEmployee.html" , context)
    else:
        return redirect('home')
