from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator

class User(AbstractUser):
    username = models.CharField(max_length=20,unique=True, validators=[MinLengthValidator(5)])
    email = models.CharField(max_length=50, unique=True, validators=[EmailValidator()])
    funds = models.DecimalField(max_digits=10, decimal_places=2, default=0)

