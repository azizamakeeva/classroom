from rest_framework import viewsets
from apps.students.models import Student
from apps.students.serializer import StudentSerializer


class StudentAPIViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


