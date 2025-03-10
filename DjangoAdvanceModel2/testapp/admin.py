from django.contrib import admin

# Register your models here.
from testapp.models import Employees

class EmpAdmin(admin.ModelAdmin):
    list_display = ['id','emp_id','emp_name','emp_addr']
admin.site.register(Employees,EmpAdmin)
