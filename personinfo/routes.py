from rest_framework import routers
from .views import PersonViewset, CarViewset

person_router = routers.DefaultRouter()
person_router.register('person', PersonViewset)

car_router = routers.DefaultRouter()
car_router.register('car', CarViewset)