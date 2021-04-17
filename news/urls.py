from rest_framework import routers

from news.views import NewsModelAPIView


router = routers.SimpleRouter()
router.register(r'news', NewsModelAPIView)
urlpatterns = [] + router.urls