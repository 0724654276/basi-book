from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.
class ContactUs(models.Model):
    """[contact model]

    Args:
        models ([class]): [create contact form]

    """
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
