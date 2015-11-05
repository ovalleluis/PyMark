from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import *


def index(request):
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render())


# Create your views here.
def supplier(request, supplier_id):
    return HttpResponse("You're looking at supplier %s" % supplier_id)

def customer(request, customer_id):
    return HttpResponse("You're looking at customer %s" % customer_id)

def rfp(request, rfp_id):
    return HttpResponse("You're looking at rfp %s" % rfp_id)