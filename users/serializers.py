from rest_framework import serializers

from .models import User


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_staff', 'last_login', 'is_superuser', ]


class ManagerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        exclude = ['groups', 'user_permissions', 'is_staff', 'last_login', 'is_superuser', 'type']

    def create(self, validated_data):
        validated_data['type'] = User.Type.MANAGER
        return super(ManagerSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['type'] = User.Type.MANAGER
        return super(ManagerSerializer, self).update(instance, validated_data)
