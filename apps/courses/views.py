from rest_framework import generics, viewsets

from apps.courses.models import Course
from apps.courses.serializer import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

