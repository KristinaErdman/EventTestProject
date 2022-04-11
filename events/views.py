from rest_framework import viewsets

from .models import FirstTypeEvent, SecondTypeEvent, Application, Feedback
from .permissions import ForManagerOrReadOnlyPermission, ForGuestOrReadOnlyPermission
from .serializers import FirstTypeEventSerializer, FirstTypeEventReadSerializer, SecondTypeEventSerializer, \
    SecondTypeEventReadSerializer, ApplicationSerializer, ApplicationReadSerializer, FeedbackSerializer, \
    FeedbackReadSerializer


class FirstTypeEventViewSet(viewsets.ModelViewSet):
    queryset = FirstTypeEvent.objects.all()
    serializer_class = FirstTypeEventSerializer
    permission_classes = (ForManagerOrReadOnlyPermission,)

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            self.serializer_class = FirstTypeEventReadSerializer
        return super(FirstTypeEventViewSet, self).dispatch(request, *args, **kwargs)


class SecondTypeEventViewSet(viewsets.ModelViewSet):
    queryset = SecondTypeEvent.objects.all()
    serializer_class = SecondTypeEventSerializer
    permission_classes = (ForManagerOrReadOnlyPermission,)

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            self.serializer_class = SecondTypeEventReadSerializer
        return super(SecondTypeEventViewSet, self).dispatch(request, *args, **kwargs)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = (ForGuestOrReadOnlyPermission,)

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Application.objects.filter(guest=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            self.serializer_class = ApplicationReadSerializer
        return super(ApplicationViewSet, self).dispatch(request, *args, **kwargs)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (ForGuestOrReadOnlyPermission,)

    def get_queryset(self):
        if not self.request.user.is_anonymous:
            return Feedback.objects.filter(guest=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            self.serializer_class = FeedbackReadSerializer
        return super(FeedbackViewSet, self).dispatch(request, *args, **kwargs)
