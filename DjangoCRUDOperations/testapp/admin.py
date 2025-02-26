from django.contrib import admin
from testapp.models import Std

# Register your models here.
class Std_admin(admin.ModelAdmin):
    list_display = ['roll','name','marks']
admin.site.register(Std,Std_admin)
