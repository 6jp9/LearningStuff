from django.contrib import admin
from testapp.models import StdDob
# Register your models here.
class StdDobAdmin(admin.ModelAdmin):
    list_display = ['name','roll_no','date_of_birth']
admin.site.register(StdDob,StdDobAdmin)
