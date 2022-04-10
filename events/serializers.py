from rest_framework import serializers

from users.serializers import ManagerSerializer, GuestSerializer
from .models import FirstTypeEvent, SecondTypeEvent, Application, Feedback


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


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class ApplicationReadSerializer(serializers.ModelSerializer):
    event = FirstTypeEventReadSerializer(read_only=True)
    guest = GuestSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                    'middle_name', 'phone_number', 'email',))

    class Meta:
        model = Application
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackReadSerializer(serializers.ModelSerializer):
    event = SecondTypeEventReadSerializer(read_only=True)
    guest = GuestSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                    'middle_name', 'phone_number', 'email',))

    class Meta:
        model = Feedback
        fields = '__all__'
