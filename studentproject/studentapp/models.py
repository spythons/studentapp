from django.db import models
from django.db.models.fields import *

# Create your models here.

class studentdetails(models.Model):
	Admission_number =models.CharField(max_length=100)
	Admission_date = models.CharField(max_length=100)
	First_name = models.CharField(max_length=100)
	Middle_name = models.CharField(max_length=100)
	Last_name = models.CharField(max_length=100)
	Course_Batch = models.CharField(max_length=100)
	Date_of_birth = models.CharField(max_length=100)
	Gender = models.CharField(max_length=100)
	Blood_group = models.CharField(max_length=100)
	Birth_place = models.CharField(max_length=100)
	Nationality = models.CharField(max_length=100)
	Mother_tongue = models.CharField(max_length=100)
	Category = models.CharField(max_length=100)
	Religion = models.CharField(max_length=100)
	Address_line1 =models.CharField(max_length=100)
	Address_line2 = models.CharField(max_length=100)
	City = models.CharField(max_length=100)
	State = models.CharField(max_length=100)
	Pin_code = models.CharField(max_length=100)
	Country = models.CharField(max_length=100)
	Phone = models.CharField(max_length=100)
	Mobile = models.CharField(max_length=100)
	Email = models.CharField(max_length=100)
	
	