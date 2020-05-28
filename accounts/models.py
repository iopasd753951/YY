from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Accounts(models.Model):
    email = models.EmailField(unique=True)
    nick_name = models.CharField(validators=[MinLengthValidator(2)], max_length=8)
    password = models.CharField(validators=[MinLengthValidator(5)], max_length=100)
    phone_number = models.CharField(max_length=12, blank=False, unique=True)
