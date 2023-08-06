from django.db import models


# Create your models here.

class Zodiac(models.Model):
    Fire = 'Fire'
    Water = 'Water'
    Earth = 'Earth'
    Air = 'Air'
    ELEMENTS = [
        (Fire, 'Fire'),
        (Water, 'Water'),
        (Earth, 'Earth'),
        (Air, 'Air'),
    ]

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    photo = models.ImageField(blank=True, null=True)
    number = models.IntegerField(default=1)
    element = models.CharField(max_length=5, choices=ELEMENTS, default='Fire')

    def __str__(self):
        return f'{self.name}'
