from django.db import models

# Create your models here.

class Company(models.Model):
	company_representative_name = models.CharField(max_length=200)
	company_name = models.CharField(max_length=200)
	company_zipcode = models.CharField(max_length=20)
	company_phone = models.CharField(max_length=20) 
	company_email = models.EmailField()
	created_on = models.DateTimeField(auto_now_add=True)
	password = models.CharField(max_length=100)   
	class Meta:
        	abstract = True

class Supplier(Company):
	pass

class Customer(Company):
	pass

class Rfp(models.Model):
	customer = models.OneToOneField(Customer)
	created_on = models.DateTimeField(auto_now_add=True)



class RfpRequirement(models.Model):
	ask = models.CharField(max_length=200)
	rfp = models.ForeignKey(Rfp)



class Pfr(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	rfp = models.ForeignKey(Rfp)



class PfrResponse(models.Model):
	bid = models.CharField(max_length=200)
	pfr = models.ForeignKey(Pfr)
	rfpRequirement = models.ForeignKey(RfpRequirement)
