from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class UserProfile(models.Model):
    PLOVDIV = 'plovdiv'
    SOFIA = 'sofia'
    VARNA = 'varna'
    BURGAS = 'burgas'
    PLEVEN = 'pleven'

    CITIES = (
        (PLOVDIV, 'Plovdiv'),
        (SOFIA, 'Sofia'),
        (VARNA, 'Varna'),
        (BURGAS, 'Burgas'),
        (PLEVEN, 'Pleven'),
    )

    profile_picture = models.ImageField(upload_to='profiles', blank=True)
    location = models.CharField(max_length=50, choices=CITIES, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Comment(models.Model):
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitter')
    text = models.TextField(blank=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    created_date = models.DateTimeField(default=timezone.now)