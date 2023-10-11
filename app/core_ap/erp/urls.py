from django.urls import path

from core_ap.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    #path('dos/', mysecondview, name='vista2'),
    #path('tres/', vistaprueba, name='vista3'),
]