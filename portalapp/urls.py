from django.urls import path
from portalapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('manage.html/', views.manage, name='manage'),
    path('signup1.html/', views.signup1, name='signup1'),
    path('signup2.html/', views.signup2, name='signup2'),
    path('login.html/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile.html/', views.profile, name='profile'),
    path('flightstatus.html/', views.flightstatus, name='flightstatus'),
    path('checkin.html/', views.checkin, name='checkin'),
    path('admin.html/', views.admin_dashboard, name='admin_dashboard'),
    path('create_flight.html/', views.create_flight, name='create_flight'),
    path('update_flight.html/<int:pk>/', views.update_flight, name='update_flight'),
    path('delete_flight.html/<int:pk>/', views.delete_flight, name='delete_flight'),
    path('search_flight.html/', views.search_flights, name='search_flights'),
    path('book_flight.html/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('payment.html/<int:flight_id>/', views.booking_invoice, name='booking_invoice'),
    path('contact_form.html/', views.contact_view, name='contact_view'),
]
