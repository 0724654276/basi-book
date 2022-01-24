from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
# Create your models here.
'''class BookModel(models.Model):
    """[BookModel]

    Args:
        models ([Class]): [Book model to book a seat]

    Returns:
        [modelDatabase]: [Create table from python class]
    """
    user_requesting = models.ForeignKey(User, on_delete=models.CASCADE)
    from_location = models.CharField(max_length=100, blank=True)
    to_location = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.user_requesting + from_location


    '''