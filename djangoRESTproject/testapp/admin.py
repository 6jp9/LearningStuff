from django.contrib import admin
from testapp.models import Movies

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','name','hero','rating']
admin.site.register(Movies,MoviesAdmin)
