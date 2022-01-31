from django.contrib import admin
from .models import Driver,Passenger,Bus,Route,Booking
# Register your models here.
admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Booking)
