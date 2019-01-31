from django.db import models
from trndy_cleaners.jobs.models import Order
from trndy_cleaners.users.models import User
# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name=_(""), on_delete=models.CASCADE)

    def __str__(self):
        return self.order