from django.urls import path
from rest_framework import routers
from news.views import NewsModelAPIView, MainPage, NewsPage, StatisticPage


router = routers.SimpleRouter()
router.register(r'news', NewsModelAPIView)
urlpatterns = [
    path('', MainPage.as_view(), name="main"),
    path('novosti/', NewsPage.as_view(), name="news"),
    path('statistika/', StatisticPage.as_view(), name="statistic"),

] + router.urls