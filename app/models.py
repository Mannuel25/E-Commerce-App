from django.db import models
from users.models import CustomUser

class Clothings(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.CharField(max_length=225, null=True, blank=True)
    discounted_price = models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PhoneAndAccessories(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.CharField(max_length=225, null=True, blank=True)
    discounted_price = models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HomeAndOffice(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    discounted_price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HealthAndBeauty(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    discounted_price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Gaming(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    discounted_price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    price = models.CharField(max_length=225, null=True, blank=True)
    discounted_price = models.CharField(max_length=225, null=True, blank=True)
    no_of_orders = models.IntegerField(default=1, null=True, blank=True)
    category = models.CharField(max_length=225, null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    total_amount = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class AllProducts(models.Model):
    categories = (
        ('Clothings', 'Clothings'),
        ('PhoneAndAccessories', 'Phone And Accessories'),
        ('HomeAndOffice', 'Home And Office'),
        ('HealthAndBeauty', 'Health And Beauty'),
        ('Gaming', 'Gaming'),
    )
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField("Categories", choices=categories, max_length=225, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    price= models.CharField(max_length=225, null=True, blank=True)
    discounted_price= models.CharField(max_length=225, null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    image_name = models.CharField(max_length=225, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.category

