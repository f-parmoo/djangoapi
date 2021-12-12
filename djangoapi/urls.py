from django.contrib import admin
from django.urls import path, include
from personinfo.routes import person_router, car_router
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(person_router.urls) ),
    path('api/', include(car_router.urls) ),
    path('graphqlapi/', GraphQLView.as_view(graphiql=True))

]
