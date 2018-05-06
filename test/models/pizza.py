from django.db import models


class Pizza(models.Model):
    pass


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, models.CASCADE)


__all__ = [
    'Pizza',
    'Topping',
]
