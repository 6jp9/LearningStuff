from django.contrib import admin

# Register your models here.
from testapp.models import Students

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['roll','name','marks']
admin.site.register(Students,StudentsAdmin)