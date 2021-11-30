from rest_framework.routers import DefaultRouter
from apps.users.views import UserAPIViewSet


router = DefaultRouter()
router.register('', UserAPIViewSet, basename='user')


urlpatterns = router.urls