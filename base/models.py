from django.db import models
import os
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

def get_image_upload_path(instance, filename):
    # Get the app name and model name
    app_name = instance._meta.app_label
    model_name = instance._meta.model_name

    # Generate the upload path based on the ID
    upload_path = os.path.join(app_name, "static", app_name , "images" , str(instance.id), filename)

    return upload_path

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title  = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    location = models.CharField(max_length=200)
    linktolocation = models.URLField(null=True,blank=True)
    public = models.BooleanField(default=True)
    date  = models.DateField(auto_now_add=True)
    rating = models.SmallIntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(5)])
    image = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date']

class Location(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
