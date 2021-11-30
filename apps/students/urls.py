from rest_framework.routers import DefaultRouter
from apps.students.views import StudentAPIViewSet

router = DefaultRouter()
router.register('', StudentAPIViewSet, basename='student')

urlpatterns = router.urls
