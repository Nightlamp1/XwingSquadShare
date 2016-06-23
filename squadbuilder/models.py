from __future__ import unicode_literals

from django.db import models

# Create your models here.

#Defining model for Expansion table
#This table will contain a list of all expansions with the following info
#   id = primary key auto created by django
#   name = name of the expansion
#   img = image path to picture of expansion
class Expansions(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    wave = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Ships(models.Model):
    name = models.CharField(max_length=50)
    expansion = models.ForeignKey(Expansions, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    faction = models.CharField(max_length=50)
    altFaction = models.CharField(max_length=50)

    def __str__(self):
        return self.name


#Defining model for the Pilots table
#This table will contain information for all pilots in the game
class Pilots(models.Model):
    name = models.CharField(max_length=50)
    pilotCost = models.IntegerField()
    expansion = models.ForeignKey(Expansions, on_delete=models.CASCADE)
    img = models.CharField(max_length=100, null=True)
    ship = models.ForeignKey(Ships, on_delete=models.CASCADE, null=True)
    isUnique = models.IntegerField()
    quantity = models.IntegerField()
    faction = models.CharField(max_length=50)
    def __str__(self):
        return (self.name).replace(" ","")

class UpgradeTypes(models.Model):
    name = models.CharField(max_length=50)

class Upgrades(models.Model):
    upgradetype = models.ForeignKey(UpgradeTypes)
    name = models.CharField(max_length=50)
    expansion = models.ForeignKey(Expansions)
    quantity = models.IntegerField()
    upgradeCost = models.IntegerField()
    isUnique = models.IntegerField()

class Pilot2Upgrades(models.Model):
    pilot = models.ForeignKey(Pilots)
    upgrade = models.ForeignKey(UpgradeTypes)
    quantity = models.IntegerField()

    def __str__(self):
        return self.upgrade.name
    
    
