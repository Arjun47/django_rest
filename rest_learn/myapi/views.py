from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GharSerializer
from .models import Ghar

# Create your views here.

class GharViewSet(viewsets.ModelViewSet):
    queryset = Ghar.objects.all().order_by('name')
    serializer_class = GharSerializer