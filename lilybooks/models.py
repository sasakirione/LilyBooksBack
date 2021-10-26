from django.db import models


class Theme(models.Model):
    theme_id = models.CharField(max_length=12)
    ndc = models.CharField(max_length=3)
    theme_title = models.CharField(max_length=32)
    theme_url = models.URLField()
    theme_explanation = models.CharField(max_length=400)
    theme_created = models.DateTimeField()


class Book(models.Model):
    user_id = models.CharField(max_length=12)
    theme_id = models.ForeignKey(Theme, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    comment = models.CharField(max_length=200)
    book_created = models.DateTimeField()


