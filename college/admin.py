from django.contrib import admin
from college import models
from . import models

# Register your models here.

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','reg_num','ph_num']
    list_editable=['reg_num','ph_num']
    ordering=['name']