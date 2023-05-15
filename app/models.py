from django.db import models
from users.models import CustomUser

class Clothings(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PhoneAndAccessories(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HomeAndOffice(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HealthAndBeauty(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Gaming(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
