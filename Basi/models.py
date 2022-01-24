from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.
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
    num_plate = models.CharField(max_length=100,blank=True)
    id_num = models.CharField(max_length=100, blank=True)
    route = models.CharField(max_length=100, blank=True)
    phone_num = models.CharField(max_length=100,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
  
    
    def __str__(self):
        return str(self.user)


    