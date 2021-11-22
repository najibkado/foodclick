from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    def serialize(self):
        return {
            "user": self.__dict__()
        }

class Entity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="entity_owner")
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    pickup_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def serialize(self):
        return {
            "user": self.user.serialize(),
            "name": self.name,
            "desc": self.desc,
            "pickup_address": self.pickup_address,
            "phone": self.phone,
            "date": str(self.date)
        }

class Listing(models.Model):
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="food_giver")
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    pickup_address = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)

class Giveaway(models.Model):
    nin = models.CharField(max_length=255)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="giveaway_listing")
    date = models.DateTimeField(auto_now=True)


