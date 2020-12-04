from django.db import models


# Create your models here.
class Device(models.Model):
    SMARTPHONE = 'smartphone'
    TABLET = 'tablet'
    LAPTOP = 'laptop'

    DEVICE_TYPE = (
        (SMARTPHONE, 'Smartphone'),
        (TABLET, 'Tablet'),
        (LAPTOP, 'Laptop')
    )

    title = models.CharField(blank=False, max_length=100)
    image = models.ImageField(upload_to='devices')
    description = models.TextField(max_length=500)
    type = models.CharField(max_length=10, choices=DEVICE_TYPE)
    brand = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)
    storage_capacity = models.IntegerField(blank=False)
    ram = models.IntegerField(blank=False)
    cpu_speed = models.FloatField(blank=False)
    os = models.CharField(max_length=50, blank=False)
    price = models.FloatField(blank=False)

    def __str__(self):
        return f"{self.title}"
