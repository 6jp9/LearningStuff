from django.contrib import admin

# Register your models here.
from testapp2.models import Base,Student,Teacher

admin.site.register(Base)
admin.site.register(Student)
admin.site.register(Teacher)
