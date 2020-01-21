from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .serializer import AttributeSerializer
from .models import Attribute
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET','POST','DELETE'])
def ShowAttribute(request):
    if request.method=='GET':
        attribute_list=Attribute.objects.all()
        seri=AttributeSerializer(attribute_list,many=True)
        return Response(seri.data)

    elif request.method=='POST':
        seri=AttributeSerializer(data=request.data)
        if seri.is_valid():
            seri.save()
        return Response(seri.data,status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
          data=Employee.objects.all()
          data.delete()
          return render(request,'application/data.html',{'data':data})
