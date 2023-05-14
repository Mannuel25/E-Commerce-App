from django.db import models

class Clothings(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.FloatField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="clothings_images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PhoneAndAccessories(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.FloatField(max_length=225, null=True, blank=True)
    in_stock =  models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="phone_accessories_images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HomeAndOffice(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.FloatField(max_length=225, null=True, blank=True)
    in_stock =  models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="home_office_images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HealthAndBeauty(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.FloatField(max_length=225, null=True, blank=True)
    in_stock =  models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="health_beauty_images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Gaming(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.FloatField(max_length=225, null=True, blank=True)
    in_stock =  models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="gaming_images/", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

