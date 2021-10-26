from django.contrib import admin

from lilybooks.models import Theme, Book


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
