from django.contrib import admin

# Register your models here.
from .models import User,CSVData

class useradmin(admin.ModelAdmin):
    list_display = ['username','email','country']

class CSVdataadmin(admin.ModelAdmin):
    list_display = ['username','email','country']

admin.site.register(User,useradmin)
admin.site.register(CSVData,CSVdataadmin)
