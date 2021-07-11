from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class ApiKey(models.Model):
    created = models.DateTimeField(auto_now=True)
    key = models.CharField(max_length=32)
    # TODO: Many-To-Many access on the data categories