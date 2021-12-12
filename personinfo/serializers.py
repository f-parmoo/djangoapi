from rest_framework import serializers
from .models import Person, Car


class CarSerializer(serializers.ModelSerializer):
    person = serializers.StringRelatedField()

    class Meta:
        model = Car
        fields = ('name', 'year', 'person')


class PersonSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'age', 'email', 'cars')
