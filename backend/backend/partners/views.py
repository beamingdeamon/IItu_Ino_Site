from django.shortcuts import render
from .models import Partner
from . import serializers

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
import json
from rest_framework import generics
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


@permission_classes((permissions.AllowAny,))
class createPartner(APIView):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        partner = Partner(imgSource = data['imgSource'], text = data['text'])
        partner.save()
        return Response(request.data)

@permission_classes((permissions.AllowAny,))
class getPartners(generics.ListAPIView):
        queryset = Partner.objects.all()
        serializer_class = serializers.PartnerSerializer

@permission_classes((permissions.AllowAny,))
class deletePartner(APIView):
        def delete(self, request, pk):
                partner = Partner.objects.get(pk=pk)
                partner.delete()
                return Response('Delete succesfull')
          
@permission_classes((permissions.AllowAny,))     
class updatePartner(APIView):
        def put(self, request,pk):
                partner = Partner.objects.get(pk=pk)
                serializer = serializers.PartnerSerializer(partner, data=request.data)
                if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)