# After creating a model, run: python manage.py makemigrations drinks
# if you get an installed app error go to settings.py and add to installed apps

from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    object = models.Manager()
    def __str__(self):
        return self.name + ' | ' + self.description
