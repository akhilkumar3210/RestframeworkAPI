from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import *
from .serializers import *
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins
from rest_framework.response import Response
# Create your views here.
def fun1(req):
    d={'name':'anu','age':22}
    return JsonResponse(d)

def f2(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=Sample(d,many=True)
        return JsonResponse(s.data,safe=False)
@csrf_exempt
def f3(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=model_serializer(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=model_serializer(data=d)
        if s.is_valid():
          s.save()
          return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
 
@csrf_exempt       
def f4(req,d):
    try:
        demo=Student.objects.gtr(pk=d)
    except Student.DoesNotExist:
        return HttpResponse('Invaild')
    if req.method=='GET':
        s=model_serializer(demo)
        return JsonResponse(s.data)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=model_serializer(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif req.method=='DELETE':
        demo.delete()
        return HttpResponse('deleted')
 
@api_view(['GET','POST'])    
def f5(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=model_serializer(d,many=True)
        return Response(s.data)
    elif req.method=='POST':
        s=model_serializer(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])        
def f6(req,d):
    try:
        demo=Student.objects.get(pk=d)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=model_serializer(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=model_serializer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
           
class f7(APIView):
    def get(self,req):
        demo=Student.objects.all()
        s=model_serializer(demo,many=True)
        return Response(s.data)
    def post(self,req):
        s=model_serializer(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
                    