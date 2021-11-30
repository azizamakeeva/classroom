from django.urls import path
from apps.courses.views import CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CourseViewSet, basename='course')

urlpatterns = router.urls
