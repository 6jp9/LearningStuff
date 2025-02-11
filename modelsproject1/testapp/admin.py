from django.contrib import admin
from testapp.models import Test_table_IT,Test_table_Gov
# Register your models here.
class ITjobAdmin(admin.ModelAdmin):
    list_display = ('name','location','salary','eligibility','link')
admin.site.register(Test_table_IT,ITjobAdmin)

class GovjobAdmin(admin.ModelAdmin):
    list_display = ('name','location','eligibility','link')
admin.site.register(Test_table_Gov,GovjobAdmin)
