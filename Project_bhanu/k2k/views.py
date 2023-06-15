from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, HttpResponse
from googletrans import Translator
from django.http import JsonResponse
from k2k.models import r_lookupdata, r_k2support, r_district_data, r_farmingassets, d_user_data, r_state_district

from .serializers import r_lookupdataSerializer, r_district_dataSerializer, r_farmingassetsSerializer, d_user_dataSerializer, r_state_districtSerializer, r_k2supportSerializer
# Create your views here.

def lookupdata(request):
    if request.method == 'GET':
        _lookupdata = r_lookupdata.objects.all()
        serializer = r_lookupdataSerializer(_lookupdata, many=True)

        return JsonResponse(serializer.data, safe=False)
    
   
def k2support(request):
    if request.method == 'GET':
        _k2support = r_k2support.objects.all()
        serializer = r_k2supportSerializer(_k2support, many=True)

        return JsonResponse(serializer.data, safe=False)
    
def district_data(request):
    if request.method == 'GET':
        _district_data = r_district_data.objects.all()
        serializer = r_district_dataSerializer(_district_data, many=True)

        return JsonResponse(serializer.data, safe=False)

def farmingassets(request):
    if request.method == 'GET':
        _farmingassets = r_farmingassets.objects.all()
        serializer = r_farmingassetsSerializer(_farmingassets, many=True)

        return JsonResponse(serializer.data, safe=False)

def user_data(request):
    if request.method == 'GET':
        _user_data = d_user_data.objects.all()
        serializer = d_user_dataSerializer(_user_data, many=True)

        return JsonResponse(serializer.data, safe=False)
    

def state_district(request):
    if request.method == 'GET':
        _state_district = r_state_district.objects.all()
        serializer = r_state_districtSerializer(_state_district, many=True)

        return JsonResponse(serializer.data, safe=False)
