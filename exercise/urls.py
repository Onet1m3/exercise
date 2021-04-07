from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from news.views import NewsModelAPIView


router = routers.DefaultRouter()
router.register(r'users', NewsModelAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/news', include(router.urls)),
]
