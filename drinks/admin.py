# Admin is completely optional

from django.contrib import admin
from .models import Drink

admin.site.register(Drink)