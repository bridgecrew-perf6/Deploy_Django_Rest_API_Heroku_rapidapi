from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import WFMTTaskModel
from .serializers import WFMTMSerializer
from rest_framework.pagination import PageNumberPagination
from .pagination import WFMTPagination
# Create your views here.

class WFMTCRUDView(ModelViewSet):
    queryset = WFMTTaskModel.objects.all()
    serializer_class = WFMTMSerializer
    pagination_class = WFMTPagination

    
