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
    cost = models.IntegerField()
    
class SquadComments(models.Model):
    comment = models.CharField(max_length=400)
    squad = models.ForeignKey(SavedSquads)
    user = models.ForeignKey(User)
    commentDate = models.DateField(default=date.today)

class UserUpvotes(models.Model):
    user = models.ForeignKey(User)
    squad = models.ForeignKey(SavedSquads)
