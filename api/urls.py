from django.conf.urls import include
from django.urls import path 
from rest_framework import routers #todo, menyediakan kelas-kelas untuk menagani routing URL dalam aplikasi ROUTING
from .views import MovieViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter() #todo, otomatis membuat URL, Navigasi API, List and Detail Views
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]