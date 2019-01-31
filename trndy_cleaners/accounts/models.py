from django.conf import settings
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name='client')
    
        

class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name='employee')
