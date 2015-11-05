from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Marketplace Index")

# Create your views here.
def supplier(request, supplier_id):
    return HttpResponse("You're looking at supplier %s" % supplier_id)

def customer(request, customer_id):
    return HttpResponse("You're looking at customer %s" % customer_id)

def rfp(request, rfp_id):
    return HttpResponse("You're looking at rfp %s" % rfp_id)