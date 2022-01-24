from django.db import models

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
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
class Passenger(models.Model):
    """[Passenger model]

    Args:
        models ([class): [model class to create user[passenger]]

    Returns:
        [python string]: [stringify the user object]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
 
    def __str__(self):
        return self.user.username


