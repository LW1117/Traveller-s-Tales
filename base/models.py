from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title  = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=200)
    linktolocation = models.URLField(null=True,blank=True)
    public = models.BooleanField(default=True)
    date  = models.DateField(auto_now_add=True)
    rating = models.SmallIntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'date'

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
