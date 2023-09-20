#from django.test import TestCase
# from app.wsgi import *
# from core_ap.erp.models import Type, Employee

# Listar

# select* from Tabla

# query = Type.objects.all()
# print(query)


#insercion
# t = Type(name='Fernando')
# #t.name = 'Bryan'
# t.save()


#edicion
# t = Type.objects.get(id=1)
# t.name = 'Accionista1'
# t.save()

#Eliminacion
# t = Type.objects.get(pk=3)
# t.delete()


#LISTAR CON FILTER

# obj = Employee.objects.filter(type_id=11)
#
# # obj = Type.objects.filter(name__icontains='Acc')
# for i in Type.objects.filter():
#     print(i.name)



