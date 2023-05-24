from django.db import models

class Asset (models.Model):
    ticker = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=70, blank=True, null=True)
    product = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=70,default='')
  