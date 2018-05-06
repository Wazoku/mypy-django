from django.db import models


class Pizza(models.Model):
    objects = models.Manager['Pizza']


class Topping(models.Model):
    objects = models.Manager['Topping']
    pizza: Pizza
