from django.contrib.auth.models import AbstractUser , PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from trndy_cleaners.users.manager import UserManager


USER_TYPE = (
    ("0","Admin"),
    ("1","Client"),
)

class User(AbstractUser ,  PermissionsMixin):
    phone_number = models.CharField(_("Phone number of the user"),max_length=100 , blank=False , unique=True)
    email = models.EmailField(_("Email of the user"),blank = False , unique=True)
    first_name = models.CharField(_("First name of the user"),max_length=255)
    last_name = models.CharField(_("Last name of the user"),max_length=255)
    user_type = models.CharField(_("Type of the user"),max_length=2 , blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

    REQUIRED_FIELDS = ['email']

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
    
    def __str__(self):
        return self.phone_number + " " + self.email
