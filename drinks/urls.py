from django.contrib import admin
from django.urls import path
from drinks.Views import drinks_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drinks/', drinks_view.drink_list),
    path('drinks/<int:_id>', drinks_view.drink_detail)
]
