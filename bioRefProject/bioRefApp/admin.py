from django.contrib import admin
from .models import InputInfo

# Register your models here.
@admin.register(InputInfo)
class UploadedInputsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'time_of_process', 'input_data', 'output_data']

