from django.db import models

# Create your models here.

class Company(models.Model):
	company_representative_name = models.CharField(max_length=200)
	company_name = models.CharField(max_length=200,unique=True)
	company_zipcode = models.CharField(max_length=20)
	company_phone = models.CharField(max_length=20) 
	company_email = models.EmailField()
	created_on = models.DateTimeField(auto_now_add=True)
	password = models.CharField(max_length=100)
	def __unicode__(self):
		return self.company_name
	class Meta:
		abstract = True


class Supplier(Company):
	pass

class Customer(Company):
	pass

class Rfp(models.Model):
    customer = models.ForeignKey(Customer)
    created_on = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.customer.__unicode__()+"-"+str(self.id)


class RfpRequirement(models.Model):
    ask = models.CharField(max_length=200)
    rfp = models.ForeignKey(Rfp)
    def __unicode__(self):
        return self.rfp.__unicode__()+"-"+str(self.id)


class Pfr(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier)
    rfp = models.ForeignKey(Rfp)
    def __unicode__(self):
        return self.supplier.__unicode__()+"-"+str(self.id)



class PfrResponse(models.Model):
    bid = models.CharField(max_length=200)
    pfr = models.ForeignKey(Pfr)
    rfpRequirement = models.ForeignKey(RfpRequirement)
    def __unicode__(self):
        return self.pfr.__unicode__()+"-"+str(self.id)
