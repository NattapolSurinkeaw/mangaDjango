from django.contrib import admin
from manga.models import Category, Cartoon, Episode

# Register your models here.
admin.site.register(Category)
admin.site.register(Cartoon)
admin.site.register(Episode)