from django.db import models

# Create your models here.
class InputInfo(models.Model):
    user_name = models.CharField(max_length=1000)
    time_of_process = models.CharField(max_length=1000)
    input_data = models.TextField()
    output_data = models.TextField() 
