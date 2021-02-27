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

class Invoice(models.Model):
    business_address = models.CharField(max_length=100)
    business_information = models.CharField(max_length=100)
    customer_information = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_reference = models.CharField(max_length=100)
    po_no = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    notes = models.TextField(max_length=1000)
    due_date = models.CharField(max_length=100)
    company_number = models.CharField(max_length=100)
    vat_number = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=100)
    sort_code_no = models.CharField(max_length=100)

    def editURL(self):
        return reverse("editInvoice", kwargs={"inv_id":self.id})
    def deleteURL(self):
        return reverse("deleteInvoice", kwargs={"inv_id":self.id})
    def downloadURL(self):
        return reverse("downloadInvoice", kwargs={"inv_id":self.id})

class Quotation(models.Model):
    business_address = models.CharField(max_length=100)
    business_information = models.CharField(max_length=100)
    customer_information = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_reference = models.CharField(max_length=100)
    po_no = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    notes = models.TextField(max_length=1000)
    due_date = models.CharField(max_length=100)
    company_number = models.CharField(max_length=100)
    vat_number = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=100)
    sort_code_no = models.CharField(max_length=100)
    notes_and_attachments = models.TextField(max_length=10000)

    def editURL(self):
        return reverse("editQuotation", kwargs={"quot_id":self.id})
    def deleteURL(self):
        return reverse("deleteQuotation", kwargs={"quot_id":self.id})
    def downloadURL(self):
        return reverse("downloadQuotation", kwargs={"quot_id":self.id})

class Report(models.Model):
    productivity_report = models.CharField(max_length=100)
    job_report = models.CharField(max_length=100)
    time_sheet_report = models.CharField(max_length=100)
    job_financial_report = models.CharField(max_length=100)
    quote_create = models.CharField(max_length=100)
    quote_expired = models.CharField(max_length=100)
    quote_converted_bad_debts = models.CharField(max_length=100)
    aged_recievables = models.CharField(max_length=100)
    one_of_jobs = models.CharField(max_length=100)
    def editURL(self):
        return reverse("editReport", kwargs={"rep_id":self.id})
    def deleteURL(self):
        return reverse("deleteReport", kwargs={"rep_id":self.id})
    def downloadURL(self):
        return reverse("downloadReport", kwargs={"rep_id":self.id})


class Scheduler(models.Model):
    choices = (
        ("RED","RED"),
        ("YELLOW", "YELLOW"),
        ("GREEN", "GREEN")
    )
    jobs = models.CharField(max_length=100)
    start_date_and_time = models.CharField(max_length=100)
    end_date_and_time = models.CharField(max_length=100)
    staff = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    schedule_calender = models.CharField(max_length=100)
    colorCode = models.CharField(max_length=100, choices=choices)

    def editURL(self):
        return reverse("editScheduler", kwargs={"sch_id":self.id})
    def deleteURL(self):
        return reverse("deleteScheduler", kwargs={"sch_id":self.id})
    def downloadURL(self):
        return reverse("downloadScheduler", kwargs={"sch_id":self.id})
