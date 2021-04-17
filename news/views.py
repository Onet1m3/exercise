from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from .models import NewsModel
from .serializers import NewsModelSerializers


class NewsModelAPIView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializers

def index(request):
    context = {}
    return render(request, "index.html", context=context)


class NewsPage(ListView):
    queryset = NewsModel.objects.all()
    template_name = "news.html"
    context_object_name = "news"
