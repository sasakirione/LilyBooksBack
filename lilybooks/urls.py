from django.urls import path
from rest_framework import routers
from .views import ThemeViewSet, BookViewSet


router = routers.DefaultRouter()
router.register(r'themes', ThemeViewSet)
router.register(r'books', BookViewSet)