from django import forms
from .models import Invoice, Quotation, Report, Scheduler

class invoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class quotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'

class reportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

class scheduelerForm(forms.ModelForm):
    class Meta:
        model = Scheduler
        fields = '__all__'