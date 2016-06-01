from __future__ import unicode_literals
from datetime import date
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class SavedSquads(models.Model):
    name = models.CharField(max_length=50)
    squadcode = models.CharField(max_length=100)
    isPublic = models.BooleanField(default=True)
    createdDate = models.DateField(default=date.today)
    user = models.ForeignKey(User)
    upvotes = models.IntegerField()
    
