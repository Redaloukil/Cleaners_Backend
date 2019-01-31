from django.db import models
from trndy_cleaners.accounts.models import Client


class Address(models.Model):
    address = models.CharField(max_length = 300)

class Geolocation(models.Model):
    longitude = models.IntegerField()
    largitude = models.IntegerField()

class Order(models.Model):
    client = models.OneToOneField(Client , on_delete=models.CASCADE)
    option1 = models.BooleanField()
    option2 = models.BooleanField()
    option3 = models.BooleanField()
    option4 = models.BooleanField()
    # date = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now=False, auto_now_add=True )
    # modified = models.DateTimeField(auto_now=True, auto_now_add=False )
    # accepted = models.BooleanField(default = False )
    # # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.client.email + " " + self.client.phone_number 


