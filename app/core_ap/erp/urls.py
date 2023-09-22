from django.urls import path

from core_ap.erp.views import myfirstview, mysecondview

app_name = 'erp'

urlpatterns = [
    path('uno/', myfirstview, name='vista1'),
    path('dos/', mysecondview, name='vista2')
]