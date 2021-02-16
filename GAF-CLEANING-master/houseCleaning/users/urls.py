from django.urls import path

from pages.views import employees, resetEMP, deleteEMP, resetAll

app_name="Employee"

urlpatterns = [
    path("reset/<int:emp_id>/",resetEMP,name="resetEmp"),
    path("delete/<int:emp_id>/",deleteEMP, name="deleteEmp"),
    path("", employees, name="employees"),
    path("reset/all/", resetAll, name="resetAll" )

]