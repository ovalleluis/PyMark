from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /core/
    url(r'^$', views.index, name='index'),
    # ex: /core/supplier/
    url(r'^supplier/(?P<supplier_id>[0-9]+)/$', views.supplier, name='supplier'),
    # ex: /core/customer/
    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.customer, name='customer'),
    # ex: /core/supplier/rfp/
    url(r'^rfp/(?P<rfp_id>[0-9]+)/$', views.rfp, name='rfp'),
]
