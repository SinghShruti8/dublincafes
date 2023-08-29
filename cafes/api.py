from rest_framework import routers

from .viewsets import CafeViewSet

router = routers.DefaultRouter()
router.register(r"cafes", CafeViewSet)

urlpatterns = router.urls
