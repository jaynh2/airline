from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser,Flight

admin.site.register(CustomUser)

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('airline', 'flight_number', 'departure', 'arrival', 'departure_time', 'arrival_time', 'price')
    search_fields = ('airline', 'flight_number', 'departure', 'arrival')


