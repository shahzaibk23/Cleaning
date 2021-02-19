from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Customer, Employee2,Employee, booking, Suppliers, create_property
from .models import Panel, ServiceDetails, ContactUs
from users.forms import SupplierForm, CreatePropertyForm

# Create your views here.

def homePage(request):
    # print(request.user.employee.employee2)
    if request.user.is_authenticated:
        userAuth = False
    else:
        userAuth = True

    if "Admin" in [g.name for g in request.user.groups.all()]:
        admin = True
    else:
        admin = False

    if "Employees" in [g.name for g in request.user.groups.all()]:
        emp = True
        emp_user = request.user.employee.employee2
    else:
        emp = False
        emp_user=None

    if "Customer" in [g.name for g in request.user.groups.all()]:
        customer = True
        cust_user = request.user.customer
    else:
        customer = False
        cust_user = None
    print(f"CUSTOMNER {customer}")
    services =  ServiceDetails.objects.all()
    context = { 
        "userAuth":userAuth,
        "user":request.user.username,
        "admin":admin,
        "customer":customer,
        "cust_user":cust_user,
        "services":services,
        "emp":emp,
        "emp_user":emp_user
    }
    return render(request, "header.html", context)

login_required(login_url='home')
def dashboard(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        bookings = booking.objects.count
        done = len([job for job in booking.objects.all() if job.status == "DONE"])
        assigned = len([job for job in booking.objects.all() if job.status == "ASSIGNED"])
        pending = len([job for job in booking.objects.all() if job.status == "IN PROGRESS"])
        context={
            "total":bookings,
            "done":done,
            "assigned":assigned,
            "pending":pending
        }
        return render(request, "dashboard.html" , context)
    else:
        return redirect('home')

login_required(login_url='home')
def customers(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        objs = Customer.objects.all()
        context = {
            "objs":objs
        }
        return render(request, "customers.html" , context)
    else:
        return redirect('home')

login_required(login_url='home')

def employees(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        objs = Employee2.objects.all()
        context = {
            "objs":objs
        }
        return render(request, "employees.html" , context)
    else:
        return redirect('home')

def viewRates(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        panel = Panel.objects.get(user=request.user)
        context={
                "panel":panel
            }
        return render(request, "rates.html", context)
    else:
        return redirect('home')

login_required(login_url='home')
def editHourlyRate(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        if request.method == 'POST':
            panel = Panel.objects.get(user=request.user).rates

            panel.hourlyRate = str(request.POST.get('hourlyRate'))
            panel.overtimeRate  =str(request.POST.get('overtimeRate'))
            panel.weekendRate  =str(request.POST.get('weekendRate'))
            panel.bankHolidayRate = str(request.POST.get('bankHolidayRate'))
            panel.specialRate = str(request.POST.get('specialRate'))
            panel.holidayPay  =str(request.POST.get('holidayPay'))
            panel.sickPay = str(request.POST.get('sickPay'))
            panel.grossPay = str(request.POST.get('grossPay'))

            

            # panel.hourlyRate = str(hourlyRate)
            # panel.overtimeRate  =str(overtimeRate)
            # panel

            panel.save()

            return redirect('rates')
        panel = Panel.objects.get(user=request.user)
        context={
            "panel":panel
        }
        return render(request, "hourlyRateForm.html" , context)
    else:
        return redirect('home')

login_required(login_url='home')
def resetEMP(request, emp_id):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        obj = Employee2.objects.get(id=emp_id)
        obj.earnings=str("0")
        obj.save()
        return redirect("Employee:employees")
    else:
        return redirect('home')

login_required(login_url='home')
def deleteEMP(request, emp_id):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        obj = Employee2.objects.get(id=emp_id)
        emp = obj.customer
        user = obj.customer.user
        obj.delete()
        emp.delete()
        user.delete()
        return redirect("Employee:employees")
    else:
        return redirect('home')

login_required(login_url='home')
def resetAll(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        objs = Employee2.objects.all()
        for obj in objs:
            obj.earnings  =str("0")
            obj.save()
        return redirect("Employee:employees")
    else:
        return redirect('home')

login_required(login_url='home')
def deleteCUST(request, cust_id):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        obj = Customer.objects.get(id=cust_id)
        user = obj.user
        user.delete()
        obj.delete()
        return redirect("customers")
    else:
        return redirect('home')
login_required(login_url='login')
def customerBookings(request, cust_id):
    if "Customer" in [g.name for g in request.user.groups.all()]:
        obj = Customer.objects.get(id=cust_id)
        bookings= obj.booking_set.all()
        number= obj.booking_set.count()
        context = {
            "bookings":bookings,
            "count":number
        }
        return render(request,"bookings.html", context)
    else:
        return redirect('home')

login_required(login_url='login')
def bookingView(request, service_id):
    if "Customer" in [g.name for g in request.user.groups.all()]:
        service =  ServiceDetails.objects.get(id=service_id)
        if request.method == "POST":
            address = str(request.POST.get('address'))
            time = str(request.POST.get('time'))
            date = str(request.POST.get('date'))
            booking.objects.create(
                service = service,
                address=address,
                time=time,
                date=date,
                status="IN PROGRESS",
                customer=request.user.customer
            )
            return redirect("booking",request.user.customer.id)

        return render(request, "bookingForm.html" ,{"service":service})
    else:
        return redirect('home')

login_required(login_url='home')
def ordersView(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        orders = booking.objects.all()
        context= {
            "orders":orders
        }
        return render(request, "orders.html", context)
    else:
        return redirect('home')

login_required(login_url='home')
def assignEmp(request):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        orders = booking.objects.all()
        unassigned = [order for order in orders if order.status == "IN PROGRESS"]
        context= {
            "orders":unassigned 
        }
        return render(request, "assignEmpList.html", context)
    else:
        return redirect('home')

login_required(login_url='home')
def assignForm(request, order_id):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        order=booking.objects.get(id=order_id)
        employees = Employee2.objects.all()
        if request.method == "POST":
            # print(Employee2.objects.get(id=int(str(request.POST.get('employee')).split("|")[0])))
            stipend= str(request.POST.get('stipend'))
            emp = Employee2.objects.get(id=int(str(request.POST.get('employee')).split("|")[0]))
            
            order.stipend = stipend
            order.employee = emp
            order.profit = str(int(order.service.price) - int(stipend))
            order.status = "ASSIGNED"
            order.save()
            return redirect("orders")
        context={
            "order":order,
            "employees":employees
        }
        return render(request, "assignEmpForm.html", context)
    else:
        return redirect('home')

login_required(login_url='home')
def empOrders(request,emp_id):
    if "Employees" in [g.name for g in request.user.groups.all()]:
        emp = Employee2.objects.get(id=emp_id)
        orders = [order for order in booking.objects.all() if order.employee == emp]
        context = {
            "orders":orders
        }
        return render(request, "EmployeeOrders.html", context)
    else:
        return redirect('home')

login_required(login_url='home')
def completedOrders(request):
    if "Employees" in [g.name for g in request.user.groups.all()]:
        emp = request.user.employee.employee2
        orders = [order for order in booking.objects.all() if order.employee == emp and order.status=="ASSIGNED"]
        context = {
            "orders":orders
        }
        return render(request, "EmpOrdersList.html", context)
    else:
        return redirect('home')

login_required(login_url='home')
def completeOrder(request, order_id):
    if "Employees" in [g.name for g in request.user.groups.all()]:
        order= booking.objects.get(id=order_id)
        order.employee.earnings = str(int(order.employee.earnings) + int(order.stipend))
        order.employee.save()
        order.status = "DONE"
        order.save()
        return redirect("empOrders", request.user.employee.employee2.id)
    else:
        return redirect('home')

login_required(login_url='home')
def contactsView(request):
    objs = ContactUs.objects.all()
    context = {
        "objs":objs
    }
    return render(request, "contacts.html", context)


login_required(login_url='home')
def SuppliersView(request):
    objs = Suppliers.objects.all()
    context = {
        "objs":objs
    }
    return render(request, "suppliers.html", context)

login_required(login_url='home')
def AddSupplierView(request):
    form = SupplierForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('suppliers')
    context = {
        "form":form
    }
    return render(request,"addSupplier.html", context )

login_required(login_url='home')
def deleteSupplierView(request, sup_id):
    if "Admin" in [g.name for g in request.user.groups.all()]:
        obj = Suppliers.objects.get(id=sup_id)
        obj.delete()
        return redirect("suppliers")
    else:
        return redirect('home')


from xhtml2pdf import pisa  
from django.http import HttpResponse
from django.template.loader import get_template

def printSuppliers(request):
    template_path = 'suppliersTable.html'
    objs = Suppliers.objects.all()
    context = {
        "objs":objs
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    return response
    
def printContacts(request):
    template_path = 'contactsTable.html'
    objs = ContactUs.objects.all()
    context = {
        "objs":objs
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    return response

def printOrders(request):
    template_path = 'ordersTable.html'
    orders = booking.objects.all()
    context= {
            "orders":orders
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    return response

def printEmployees(request):
    template_path = 'employeesTable.html'
    objs = Employee2.objects.all()
    context = {
        "objs":objs
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    return response

def printCustomers(request):
    template_path = 'customersTable.html'
    objs = Customer.objects.all()
    context = {
        "objs":objs
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    return response

def printRates(request):
    template_path = 'ratesTable.html'
    bookings = booking.objects.count
    done = len([job for job in booking.objects.all() if job.status == "DONE"])
    assigned = len([job for job in booking.objects.all() if job.status == "ASSIGNED"])
    pending = len([job for job in booking.objects.all() if job.status == "IN PROGRESS"])
    context={
        "total":bookings,
        "done":done,
        "assigned":assigned,
        "pending":pending
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    return response


def CreatePropertyView(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    form = CreatePropertyForm(request.POST)
    
    
    if form.is_valid():
        ob = form.save()
        ob.customer = customer
        ob.save()
        return redirect("customers")
    context={
        "customer":customer,
        "form":form,
        
    }
    return render(request, "create_property.html", context)

def viewPropertyView(request, cust_id):
    ob = Customer.objects.get(id=cust_id)
    obj = ob.create_property
    context = {
        "ob":ob,
        "obj":obj
    }
    return render(request, "viewProperty.html", context)
