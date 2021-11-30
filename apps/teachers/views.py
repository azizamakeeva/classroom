from django.shortcuts import render
from rest_framework import viewsets
from apps.teachers.models import Teacher
from apps.teachers.serializer import TeacherSerializer, TeacherCreateSerializer


class TeacherAPIViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


def get_serializer_class(self):
    if self.action in ['create']:
        return TeacherCreateSerializer
    return self.serializer_class
