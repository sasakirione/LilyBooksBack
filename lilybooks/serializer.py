from rest_framework import serializers

from .models import Theme, Book


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('theme_id', 'ndc', 'theme_title', 'theme_url', 'theme_explanation', 'theme_created')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('user_id', 'theme_id', 'isbn', 'comment', 'book_created')