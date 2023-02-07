from rest_framework import status
from rest_framework.response import Response
from drinks import serializers
from rest_framework.decorators import api_view
from drinks.Services.drinks_service import DrinksService


_service = DrinksService()


@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        return _service.get_all_drinks()

    elif request.method == 'POST':
        return _service.insert_drink(request.data)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, _id):
    if request.method == 'GET':
        return _service.get_drink_id(_id)

    elif request.method == 'PUT':
        return _service.update_drink_by_id(_id, request.data)

    elif request.method == 'DELETE':
        return _service.delete_drink_by_id(_id)
