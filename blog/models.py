from __future__ import unicode_literals

from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title


#Defining model for Expansion table
#This table will contain a list of all expansions with the following info
#   id = primary key auto created by django
#   name = name of the expansion
#   img = image path to picture of expansion
class Expansions(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Ships(models.Model):
    name = models.CharField(max_length=50)
    expansion = models.ForeignKey(Expansions, on_delete=models.CASCADE)
    quantity = models.IntegerField



#Defining model for the Pilots table
#This table will contain information for all pilots in the game
class Pilots(models.Model):
    name = models.CharField(max_length=50)
    pilotCost = models.IntegerField
    expansion = models.ForeignKey(Expansions, on_delete=models.CASCADE)
    img = models.CharField(max_length=100, null=True)
    ship = models.ForeignKey(Ships, on_delete=models.CASCADE, null=True)
    isUnique = models.IntegerField
    quantity = models.IntegerField
    




