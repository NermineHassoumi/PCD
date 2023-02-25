from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Credit.models import Demande
from Credit.serializers import DemandeSerializer
# Create your views here.

@csrf_exempt
def demandeApi(request,id=0):
    if request.method=='GET':
        demande=Demande.objects.all()
        demande_serializer=DemandeSerializer(demande,many=True)
        return JsonResponse(demande_serializer.data, safe=False )
    
    elif request.method=='POST':
        demande_data=JSONParser().parse(request) 
        demande_serializer=DemandeSerializer(data=demande_data)
        if demande_serializer.is_valid():
            demande_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method=='PUT':
        demande_data=JSONParser().parse(request)
        demande=Demande.objects.get(DemandeId=demande_data['DemandeId'])
        demande_serializer=DemandeSerializer(demande,data=demande_data)
        if demande_serializer.is_valid():
            demande_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", saf=False)
    
    elif request.method=='DELETE':
        demande=Demande.objects.get(DemandeId=id)
        demande.delete()
        return JsonResponse("Deleted Successfully!", safe=False)
