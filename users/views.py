from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, ManagerSerializer


class UserViewSet(viewsets.ModelViewSet):
    fields = ['id', 'last_login', 'is_superuser', 'is_active', 'date_joined', 'last_name', 'first_name',
              'middle_name', 'phone_number', 'email', 'password']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(
            instance,
            fields=filter(lambda field: field != 'password', self.fields)
        )

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(
                page,
                many=True,
                fields=filter(lambda field: field != 'password', self.fields)
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(
            queryset,
            many=True,
            fields=filter(lambda field: field != 'password', self.fields)
        )
        return Response(serializer.data)


class ManagerViewSet(UserViewSet):
    queryset = User.objects.filter(type=User.Type.MANAGER)
    serializer_class = ManagerSerializer


class GuestViewSet(UserViewSet):
    queryset = User.objects.filter(type=User.Type.GUEST)
    fields = ['id', 'last_login', 'is_superuser', 'is_active', 'date_joined', 'last_name', 'first_name',
              'middle_name', 'phone_number', 'email', 'password']

    serializer_class = UserSerializer
