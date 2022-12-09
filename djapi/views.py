from django.shortcuts import render
from djapi.models import Parking
from rest_framework.exceptions import NotFound
from djapi.serializers import ParkingSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['plate_number']
