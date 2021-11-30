from rest_framework import viewsets
from apps.users.models import User
from apps.users.serializer import UserSerializer


class UserAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

