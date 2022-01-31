from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import Route,Bus
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.

class Busi(models.Model):
    

    bus_name = models.CharField(max_length=25)

    image = models.ImageField(default='bus.jpg', upload_to='bus_pics')

    def __str__(self):
        return f'{self.bus.busname} Bus' 
    
    def delete_bus(self):
        self.delete()

class Ticket(models.Model):
    route_id=models.ForeignKey(Route,on_delete=models.CASCADE)        
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    #seat_id = models.ForeignKey(Seats, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    id_no = models.IntegerField(default=1)
