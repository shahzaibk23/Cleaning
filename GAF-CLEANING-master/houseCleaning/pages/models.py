from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Rates(models.Model):
    hourlyRate = models.CharField(max_length=10)
    overtimeRate = models.CharField(max_length=10)
    weekendRate  =models.CharField(max_length=10)
    bankHolidayRate = models.CharField(max_length=10)
    specialRate = models.CharField(max_length=10)
    holidayPay = models.CharField(max_length=10)
    sickPay = models.CharField(max_length=10)
    grossPay = models.CharField(max_length=10)

# Create your models here.
class Panel(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    rates = models.OneToOneField(Rates, null=True, blank=True, on_delete=models.CASCADE)


    # user = models.OneToOneField(Panel,null=True, blank=True, on_delete=models.CASCADE)
class ServiceDetails(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def getURL(self):
        return reverse("book", kwargs={"service_id":self.id})

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)

