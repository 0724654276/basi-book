from django.db import models

# Create your models here.

class Busi(models.Model):
    
    bus = models.OneToOneField(Bus, on_delete=models.CASCADE)
    image = models.ImageField(default='bus.jpg', upload_to='bus_pics')

    def __str__(self):
        return f'{self.bus.busname} Bus' 
    
    def save_profile(self):
        super().save()

    @classmethod
    def get_bus(cls):
        bus = Busi.objects.all()
        return Busi

    @classmethod
    def find_bus(cls,search_term):
        bus = Busi.objects.filter(bus__busname__icontains=search_term)
        return bus

        