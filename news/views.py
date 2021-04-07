from django.shortcuts import render

from rest_framework import viewsets

from .models import NewsModel
from .serializers import NewsModelSerializers


class NewsModelAPIView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializers
