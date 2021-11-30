from rest_framework import serializers
from apps.students.models import Student
from apps.users.serializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    student = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'student', 'hobby', ]
