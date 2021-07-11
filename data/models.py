from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class DataCategory(models.Model):
    created = models.DateTimeField('created', auto_now=True)
    creator = models.ForeignKey(User, models.CASCADE)
    type = models.CharField(max_length=8)
    
class DataRecord(models.Model):
    created = models.DateTimeField('created', auto_now=True)
    value = models.TextField('value')
    category = models.ForeignKey(DataCategory, models.CASCADE)