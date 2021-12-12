import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Car, Person


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class CarType(DjangoObjectType):
    class Meta:
        model = Car


class Query(ObjectType):
    persons = graphene.List(PersonType)
    cars = graphene.List(CarType)
    person = graphene.Field(PersonType, id=graphene.Int(required=True))
    car = graphene.Field(CarType, id=graphene.Int(required=True))

    def resolve_persons(root, info):
        return Person.objects.all()

    def resolve_cars(root, info):
        return Car.objects.all()

    def resolve_person(root, info, **kwargs):
        if kwargs.get('id'):
            return Person.objects.get(id=kwargs.get('id'))
        return None

    def resolve_car(root, info, **kwargs):
        if kwargs.get('id'):
            return Car.objects.get(id=kwargs.get('id'))
        return None


class PersonInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    age = graphene.Int()
    email = graphene.String(required=True)


class CreatePerson(graphene.Mutation):
    person = graphene.Field(PersonType)
    ok = graphene.Boolean(default_value=False)

    class Arguments:
        input = PersonInput(required=True)

    def mutate(root, info, input):
        person1 = Person.objects.create(first_name=input.get('first_name'),
                                        last_name=input.get('last_name'),
                                        age=input.get('age'),
                                        email=input.get('email'))
        return CreatePerson(person=person1, ok=True)


class CarInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    year = graphene.Int(required=True)
    person = graphene.Int()


class CreateCar(graphene.Mutation):
    car = graphene.Field(CarType)
    ok = graphene.Boolean(default_value=False)

    class Arguments:
        input = CarInput(required=True)

    def mutate(root, info, input):
        person = Person.objects.get(id=input.get('person'))
        car1 = Car.objects.create(name=input.get('name'),
                                  year=input.get('year'),
                                  person=person)
        return CreateCar(car=car1, ok=True)


class Mutation(ObjectType):
    create_person = CreatePerson.Field()
    create_car = CreateCar.Field()
