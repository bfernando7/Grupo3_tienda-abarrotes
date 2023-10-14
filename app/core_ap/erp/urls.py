from django.urls import path

from core_ap.erp.views.category.views import *

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    #path('dos/', mysecondview, name='vista2'),
    #path('tres/', vistaprueba, name='vista3'),
]