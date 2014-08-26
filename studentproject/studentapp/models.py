from django.db import models
from django.db.models.fields import *

# Create your models here.

class studentdetails(models.Model):
	Name = models.CharField(max_length=100)
	Class =models.IntegerField(max_length=100)
	Admission_id =models.CharField(max_length=100)
	Gender = models.CharField(max_length=100)
	Nationality = models.CharField(max_length=100)
	Language = models.CharField(max_length=100)
	Category = models.CharField(max_length=100)
	Religion = models.CharField(max_length=100)
	Address = models.CharField(max_length=100)
	State = models.CharField(max_length=100)
	Country = models.CharField(max_length=100)
	Phone = models.CharField(max_length=100)