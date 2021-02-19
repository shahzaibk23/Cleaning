from django.contrib import admin
from .models import Customer, Employee, Employee2, booking, Suppliers, create_property

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Employee2)
admin.site.register(booking)
admin.site.register(Suppliers)
admin.site.register(create_property)