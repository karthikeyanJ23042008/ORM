from django.db import models
from django.contrib import admin
class Infobikes_DB(models.Model):
    Bike_number=models.IntegerField()
    Name=models.CharField(max_length=10)
    Mobile_Number=models.IntegerField()
    Thingsto_repair=models.CharField(max_length=30)
    dateof_given=models.DateField()
    dateto_submit=models.DateField()
    register_number=models.IntegerField()
    total_cost=models.FloatField(primary_key=True)
class Infobikes_DBAdmin(admin.ModelAdmin):
    list_display=["Bike_number","Name","Mobile_Number","Thingsto_repair","dateof_given","dateto_submit","register_number","total_cost"]
