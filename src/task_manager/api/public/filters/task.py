from django_filters import rest_framework as filters

from task_manager.models import Task


__all__ = [
    'TaskFilter',
]


class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    start_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['title', 'start_date', 'end_date']
