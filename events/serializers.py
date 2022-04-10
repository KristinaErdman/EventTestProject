from rest_framework import serializers

from users.serializers import ManagerSerializer
from .models import FirstTypeEvent, SecondTypeEvent


class FirstTypeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstTypeEvent
        fields = '__all__'


class FirstTypeEventReadSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                        'middle_name', 'phone_number', 'email',))

    class Meta:
        model = FirstTypeEvent
        fields = '__all__'


class SecondTypeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondTypeEvent
        fields = '__all__'


class SecondTypeEventReadSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                        'middle_name', 'phone_number', 'email',))

    class Meta:
        model = SecondTypeEvent
        fields = '__all__'
