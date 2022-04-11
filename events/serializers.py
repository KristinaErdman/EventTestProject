from rest_framework import serializers

from users.serializers import UserSerializer
from .models import FirstTypeEvent, SecondTypeEvent, Application, Feedback


class FirstTypeEventSerializer(serializers.ModelSerializer):
    manager = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FirstTypeEvent
        fields = '__all__'


class FirstTypeEventReadSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                     'middle_name', 'phone_number', 'email',))

    class Meta:
        model = FirstTypeEvent
        fields = '__all__'


class SecondTypeEventSerializer(serializers.ModelSerializer):
    manager = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SecondTypeEvent
        fields = '__all__'


class SecondTypeEventReadSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                     'middle_name', 'phone_number', 'email',))

    class Meta:
        model = SecondTypeEvent
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    guest = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Application
        fields = '__all__'


class ApplicationReadSerializer(serializers.ModelSerializer):
    event = FirstTypeEventSerializer(read_only=True)
    guest = UserSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                   'middle_name', 'phone_number', 'email',))

    class Meta:
        model = Application
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    guest = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackReadSerializer(serializers.ModelSerializer):
    event = SecondTypeEventReadSerializer(read_only=True)
    guest = UserSerializer(read_only=True, fields=('id', 'is_active', 'last_name', 'first_name',
                                                   'middle_name', 'phone_number', 'email',))

    class Meta:
        model = Feedback
        fields = '__all__'
