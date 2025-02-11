from django.contrib import admin
from testapp.models import emp

class empAdmin(admin.ModelAdmin):
    list_display = ['empName','empID','empAddress','empContact']
admin.site.register(emp,empAdmin)

# Register your models here.
