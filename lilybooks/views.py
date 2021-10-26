from django.shortcuts import render
from rest_framework import viewsets

from lilybooks.models import Theme, Book
from lilybooks.serializer import ThemeSerializer, BookSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
