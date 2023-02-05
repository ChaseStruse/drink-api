# Admin is completely optional

from django.contrib import admin
from drinks.Models.drink import Drink

admin.site.register(Drink)