from django.contrib import admin
from testapp.models import Movies
# Register your models here.
class Movies_Admin(admin.ModelAdmin):
    list_display = ['name','director','rating']
admin.site.register(Movies,Movies_Admin)