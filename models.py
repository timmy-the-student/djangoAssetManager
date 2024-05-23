from django.db import models
from django_resized import ResizedImageField

class asset(models.Model):

    Name = models.CharField(max_length=25)

    Area = models.CharField(max_length=30)

    Image = ResizedImageField(upload_to='teacher images')

    Location = models.CharField(max_length=30, default='Unknown')

    LastUpdated = models.DateTimeField(auto_now=True)

class default(models.Model):

    Name = models.CharField(max_length=25)

    Area = models.CharField(max_length=30)

    Image = models.ImageField(upload_to='')

    Location = models.CharField(max_length=30, default='Unknown')