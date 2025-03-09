from django.contrib import admin

# Register your models here.
from testapp3.models import Person,Employee,Manager,C
admin.site.register(Person)
admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(C)

