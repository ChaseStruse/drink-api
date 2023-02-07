from typing import List

from rest_framework import status
from rest_framework.response import Response

from drinks import serializers
from drinks.Models.drink import Drink


class DrinksService():

    def __get_drink_object_by_id(self, _id: int) -> Drink:
        try:
            drink = Drink.object.get(pk=_id)
            return drink
        except:
            raise Exception(f'No drink found with id of {_id}')

    @staticmethod
    def get_all_drinks() -> Response:
        drinks = Drink.object.all()
        serializer = serializers.DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    @staticmethod
    def insert_drink(_data):
        serializer = serializers.DrinkSerializer(data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_drink_id(self, _id: int) -> Response:
        drink = self.__get_drink_object_by_id(_id)
        serializer = serializers.DrinkSerializer(drink)
        return Response(serializer.data)


    def update_drink_by_id(self, _id: int, _data) -> Response:
        drink = self.__get_drink_object_by_id(_id)
        serializer = serializers.DrinkSerializer(drink, data=_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete_drink_by_id(self, _id: int) -> Response:
        drink = self.__get_drink_object_by_id(_id)
        drink.delete()
        return Response(status.HTTP_204_NO_CONTENT)
