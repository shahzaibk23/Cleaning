
from django.contrib import admin
from django.urls import path, include
from users.views import SignUp,Login, Logout, addEmployees, carehomes, carpets, events, pbandc, pwss, pubsandclubs, retail, schoolcu, sportsleisure, window, vacateproperty, aboutus, contactus, datap, envip, privatep, socialp 
from pages.views import homePage,viewRates,contactsView, completedOrders, completeOrder, ordersView,assignForm,empOrders, assignEmp ,dashboard, customers, editHourlyRate, deleteCUST, customerBookings, bookingView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignUp, name="signup"),
    path('login/', Login, name="login"),
    path('carehomes/', carehomes, name="carehomes"),
    path('events/', events, name="events"),
    path('carpets/', carpets, name="carpets"),
    path('post_building_and_construction/', pbandc, name="pbandc"),
    path('pressure-washing-scrubbing-sweeping/', pwss, name="pwss"),
    path('pubsandclubs/', pubsandclubs, name="pubsandclubs"),
    path('retail/', retail, name="retail"),
    path('school-college-universities/', schoolcu, name="schoolcu"),
    path('sports-leisure/', sportsleisure, name="sportsleisure"),
    path('window/', window, name="window"),
    path('vacateproperty/', vacateproperty, name="vacateproperty"),
    path('About-Us/', aboutus, name="aboutus"),
    path('Contact-Us/', contactus, name="contactus"),
    path('Data-Policy/', datap, name="datap"),
    path('Environmental-Policy/', envip, name="envip"),
    path('Private-Policy/', privatep, name="privatep"),
    path('Soical-Media-Policy/', socialp, name="socialp"),
    path("", homePage, name='home'),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", Logout, name='logout'),
    path("customers/", customers, name='customers'),
    path("customers/delete/<int:cust_id>",deleteCUST, name="deleteCust" ),
    path("addEmployee/", addEmployees, name='addEmployee'),
    # path("employees/", employees, name="employees"),
    path("employees/", include("users.urls")),
    path("editRates/", editHourlyRate, name="editRates"),
    path("rates/", viewRates, name="rates"),
    path("customers/<int:cust_id>/bookings/",customerBookings, name="booking" ),
    path("book/<int:service_id>/", bookingView, name="book"),
    path("allOrders/", ordersView, name="orders"),
    path("assignEmp/", assignEmp, name="assignEmp"),
    path("assignEmp/<int:order_id>/",assignForm ,name="assign"),
    path("EmpOrders/<int:emp_id>/", empOrders, name="empOrders"),
    path("completeOrder/<int:order_id>", completeOrder, name="completeOrder"),
    path("completedOrders/", completedOrders, name="completedOrders"),
    path("contacts/", contactsView, name="contacts")

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
