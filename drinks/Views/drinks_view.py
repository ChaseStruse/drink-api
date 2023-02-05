from rest_framework import status
from rest_framework.response import Response
from drinks.Models.drink import Drink
from drinks import serializers
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.object.all()
        serializer = serializers.DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, _id):
    try:
        drink = Drink.object.get(pk=_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status.HTTP_204_NO_CONTENT)
