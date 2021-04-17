from django.urls import path
from rest_framework import routers
from news.views import NewsModelAPIView, MainPage, NewsPage


router = routers.SimpleRouter()
router.register(r'news', NewsModelAPIView)
urlpatterns = [
    path('', MainPage.as_view(), name="main"),
    path('novosti/', NewsPage.as_view(), name="news")

] + router.urls