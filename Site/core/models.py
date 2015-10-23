from django.db import models

# Create your models here.

class Supplier(models.Model):
    company_representative_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    company_zipcode = models.CharField(max_length=20)
    company_phone = models.CharField(max_length=20) 
    company_email = models.EmailField()
    password = models.CharField(max_length=100)   

