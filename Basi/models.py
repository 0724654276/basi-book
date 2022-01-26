from django.db import models

# Create your models here.

class Busi(models.Model):
    

    bus_name = models.CharField(max_length=25)

    image = models.ImageField(default='bus.jpg', upload_to='bus_pics')

    def __str__(self):
        return f'{self.bus.busname} Bus' 
    
    def delete_bus(self):
        self.delete()
    

        