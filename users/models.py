from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime
class User(AbstractUser):
    """[Abstract class]

    Args:
        AbstractUser ([class]): [Abstarct class to create two custom users]
    """
    is_passenger = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)

class Driver(models.Model):
    """[Driver model]

    Args:
        models ([class]): [Create a user[driver]]
    Returns:
        [python string]: [stringify user[driver] object]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return self.user.username


class Passenger(models.Model):
    """[Passenger model]

    Args:
        models ([class): [model class to create user[passenger]]

    Returns:
        [python string]: [stringify the user[passenger] object]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
 
    def __str__(self):
        return self.user.username


class Route(models.Model):
    """[summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    destination = models.CharField(max_length=100, blank=True)
    pickup_point = models.CharField(max_length=100, blank=True)

class Bus(models.Model):
    """[BookModel]

    Args:
        models ([Class]): [Book model to post a bus]

    Returns:
        [modelDatabase]: [Create table from python class]
    """
    class Seats(models.TextChoices):
        vip_seat = '1', "VIP"
        business = '2', "BUSSINESS"
        economy = '3', "ECONOMY"

  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    schedule = models.DateTimeField(default='null')
    seats = models.CharField(max_length=9,choices = Seats.choices,default=Seats.business)
    num_plate = models.CharField(max_length=100,blank=True)
    phone_num = models.CharField(max_length=100,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
  
    
    def __str__(self):
        return str(self.user)


    