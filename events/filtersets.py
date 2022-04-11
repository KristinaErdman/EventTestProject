from django_filters import FilterSet, DateFilter

from .models import Application, Feedback


class ApplicationFilterSet(FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Application
        fields = ('guest', 'event', 'date',)


class FeedbackFilterSet(FilterSet):
    start_date = DateFilter(field_name='date', lookup_expr='gte')
    end_date = DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Feedback
        fields = ('guest', 'event', 'date',)
