from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from pages.models import ServiceDetails

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    user = models.OneToOneField(User, blank=True, null=True, on_delete = models.CASCADE)

    def deleteURL(self):
        return reverse("deleteCust", kwargs={"cust_id":self.id})

    def bookingsURL(self):
        return reverse("booking", kwargs={"cust_id":self.id})
        




class Employee(models.Model):
    surname = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    full_address = models.CharField(max_length=80)
    postcode = models.CharField(max_length=20)
    tel_number = models.CharField(max_length=20)
    mob_number = models.CharField(max_length=20)
    next_of_kin = models.CharField(max_length=50)
    training_levels = models.CharField(max_length=20)
    site_stationed = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    line_supervisor =models.CharField(max_length=40)
    line_manager= models.CharField(max_length=60)
    user = models.OneToOneField(User, blank=True, null=True, on_delete = models.CASCADE)

class Employee2(models.Model):
    customer = models.OneToOneField(Employee, null=True, blank=True, on_delete=models.CASCADE)
    earnings = models.CharField(max_length=10, default="0")

    def resetURL(self):
        return reverse("Employee:resetEmp", kwargs={"emp_id":self.id})

    def deleteURL(self):
        return reverse("Employee:deleteEmp", kwargs={"emp_id":self.id})

    def ordersURL(self):
        return reverse("empOrders", kwargs={"emp_id":self.id})


class booking(models.Model):
    service = models.ForeignKey(ServiceDetails, null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer,null=True, blank=True, on_delete=models.CASCADE)
    stipend = models.CharField(max_length=50, null=True, blank=True)
    employee = models.ForeignKey(Employee2, null=True, blank=True, on_delete=models.CASCADE)
    profit = models.CharField(max_length=50, null=True, blank=True)

    def assignURL(self):
        return reverse("assign", kwargs={"order_id":self.id})
    def completeURL(self):
        return reverse("completeOrder", kwargs={"order_id":self.id})

