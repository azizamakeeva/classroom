from rest_framework.routers import DefaultRouter
from apps.teachers.views import TeacherAPIViewSet

router = DefaultRouter()
router.register('', TeacherAPIViewSet, basename='teacher')

urlpatterns = router.urls
