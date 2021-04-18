from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets

from django.contrib.auth.models import User

from .models import NewsModel
from .serializers import NewsModelSerializers


class NewsModelAPIView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelSerializers


class MainPage(ListView):
    queryset = NewsModel.objects.all()
    template_name = "index.html"
    context_object_name = "item"


class NewsPage(ListView):
    queryset = NewsModel.objects.all()
    template_name = "news.html"
    context_object_name = "news"


class StatisticPage(ListView):
    queryset = NewsModel.objects.all()
    template_name = "statistic.html"
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_user = User.objects.all()
        context["users"] = [(f"{i.username} -> ({NewsModel.objects.filter(author__username=i.username).count()})") for i in list_user]
        return context
    
