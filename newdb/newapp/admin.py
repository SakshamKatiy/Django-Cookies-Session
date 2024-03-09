from django.contrib import admin
from .models import students
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(students)

class studentAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','location')