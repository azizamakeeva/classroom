from rest_framework import serializers
from apps.teachers.models import Teacher
from apps.users.serializer import UserSerializer


class TeacherSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'teacher', 'exp']


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher', 'exp']
