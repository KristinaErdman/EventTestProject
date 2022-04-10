from rest_framework import viewsets

from .models import FirstTypeEvent, SecondTypeEvent
from .serializers import FirstTypeEventSerializer, FirstTypeEventReadSerializer, SecondTypeEventSerializer, \
    SecondTypeEventReadSerializer


class FirstTypeEventViewSet(viewsets.ModelViewSet):
    queryset = FirstTypeEvent.objects.all()
    serializer_class = FirstTypeEventSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            self.serializer_class = FirstTypeEventReadSerializer
        return super(FirstTypeEventViewSet, self).dispatch(request, *args, **kwargs)


class SecondTypeEventViewSet(viewsets.ModelViewSet):
    queryset = SecondTypeEvent.objects.all()
    serializer_class = SecondTypeEventSerializer

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            self.serializer_class = SecondTypeEventReadSerializer
        return super(SecondTypeEventViewSet, self).dispatch(request, *args, **kwargs)
