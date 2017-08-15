from django.db import models


class HomeImage(models.Model):
    banner_one = models.ImageField(upload_to='', blank=True)
    banner_two = models.ImageField(upload_to='', blank=True)
    banner_three = models.ImageField(upload_to='', blank=True)
    banner_four = models.ImageField(upload_to='', blank=True)
    banner_five = models.ImageField(upload_to='', blank=True)
    banner_six = models.ImageField(upload_to='', blank=True)
    banner_seven = models.ImageField(upload_to='', blank=True)
    banner_eight = models.ImageField(upload_to='', blank=True)
    banner_nine = models.ImageField(upload_to='', blank=True)
    banner_ten = models.ImageField(upload_to='', blank=True)


class Slider(models.Model):
    slider_image = models.ImageField(upload_to='', blank=True)