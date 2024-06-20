from django.conf.urls import include
from django.urls import path 
from rest_framework import routers #todo, menyediakan kelas-kelas untuk menagani routing URL dalam aplikasi ROUTING

router = routers.DefaultRouter() #todo, otomatis membuat URL, Navigasi API, List and Detail Views

urlpatterns = [
    path('', include(router.urls)),
]