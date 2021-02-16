from django.contrib import admin
from .models import Rates, Panel, ServiceDetails, ContactUs
# Register your models here.

admin.site.register(Rates)
admin.site.register(Panel)
admin.site.register(ServiceDetails)
admin.site.register(ContactUs)
# admin.site.register(Services)