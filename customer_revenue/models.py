from django.db import models

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class fist(models.Model):
    name = models.CharField(max_length=122)
    Administrative = models.FloatField()
    Informational = models.FloatField()
    ProductRelated = models.FloatField()
    BounceRates = models.FloatField()
    ExitRates = models.FloatField()
    PageValues = models.FloatField()
    SpecialDay = models.FloatField()
    OperatingSystems = models.IntegerField()
    Browser = models.IntegerField()
    Region = models.IntegerField()
    TrafficType = models.IntegerField()
    weekend = models.IntegerField()
    VisitorType = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name


# name = models.CharField(max_length=122)
# Administrative = models.FloatField()
# Informational = models.FloatField()
# ProductRelated = models.FloatField()
# BounceRates = models.FloatField()
# ExitRates = models.FloatField()
# PageValues = models.FloatField()
# SpecialDay = models.FloatField()
# OperatingSystems = models.IntegerField()
# Browser = models.IntegerField()
# Region = models.IntegerField()
# TrafficType = models.IntegerField()
# weekend = models.IntegerField()
# VisitorType = models.IntegerField()
# date = models.DateField()
