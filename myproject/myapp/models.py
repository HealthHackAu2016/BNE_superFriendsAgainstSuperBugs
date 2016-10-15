# -*- coding: utf-8 -*-
from django.db import models


class Sample(models.Model):
    date = models.DateField()
    hospital = models.CharField(max_length=15)
    doctor = models.CharField(max_length=25)
    gender = models.IntegerField()
    age_group = models.IntegerField()
    postcode = models.IntegerField()
    country = models.CharField(max_length=3)
    travel_last_6_m = models.CharField(max_length=3)
    condition = models.TextField()
    allergies_ab = models.TextField()
    current_ab = models.TextField()
