from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    starting_bid = models.FloatField(null=True)
    image_url = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, blank=True, related_name="category")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    listing = models.ForeignKey(Listing, null=True, blank=True, on_delete=models.SET_NULL)
    
class Bid(models.Model):
    bid = models.FloatField(null=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    listing = models.ForeignKey(Listing, null=True, blank=True, on_delete=models.SET_NULL)

