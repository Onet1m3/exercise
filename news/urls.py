from django.urls import path
from rest_framework import routers
from news.views import NewsModelAPIView, index, NewsPage


router = routers.SimpleRouter()
router.register(r'news', NewsModelAPIView)
urlpatterns = [
    path('', index, name="main"),
    path('novosti/', NewsPage.as_view(), name="news")

] + router.urls