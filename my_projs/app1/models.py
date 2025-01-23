from django.db import models

# Create your models here.

class app1_model(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    phone_number = models.IntegerField()