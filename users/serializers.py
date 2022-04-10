from rest_framework import serializers

from .models import Manager, Guest


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ManagerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Manager
        exclude = ['groups', 'user_permissions', 'is_staff', 'last_login', 'is_superuser', ]


class GuestSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Guest
        exclude = ['groups', 'user_permissions', 'is_staff', 'last_login', 'is_superuser', ]
