from django.db import models
from django.core.validators import MinLengthValidator


class Accounts(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(validators=[MinLengthValidator(5)], max_length=255)
    password = models.CharField(validators=[MinLengthValidator(5)], max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
