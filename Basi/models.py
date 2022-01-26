from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from users.models import Route,Bus,Seats

# Create your models here.

class Ticket(models.Model):
    route_id=models.ForeignKey(Route,on_delete=models.CASCADE)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seats, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    id_no = models.IntegerField(default=1)