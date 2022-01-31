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

class BusModel(models.Model):
    """[BookModel]

    Args:
        models ([Class]): [Book model to post a bus]

    Returns:
        [modelDatabase]: [Create table from python class]
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='bus_pics/')
    location = models.CharField(max_length=100, blank=True)
    seats = models.CharField(max_length=100, blank=True)
    first_class = models.CharField(max_length=100, blank=True)
    second_class = models.CharField(max_length=100, blank=True)
    regular_class = models.CharField(max_length=100, blank=True)
    num_plate = models.CharField(max_length=100,blank=True)
    id_num = models.CharField(max_length=100, blank=True)
    route = models.CharField(max_length=100, blank=True)
    phone_num = models.CharField(max_length=100,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
  
    
    def __str__(self):
        return str(self.user)




class BookingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(BusModel, on_delete=models.CASCADE)
    # time = models.
    no_of_seats = models.IntegerField(default=0)
    route = models.CharField(max_length=200) 
    date_booked = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return str(self.user)

    