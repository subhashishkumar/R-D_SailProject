import django_filters
from inputforms.models import *
from django_filters import STRICTNESS
from django_filters.widgets import RangeWidget


class AllAccdFilter(django_filters.FilterSet):
    Date = django_filters.DateFromToRangeFilter(widget=RangeWidget())

    class Meta:
        model = AllAccident
        fields = ['cause', 'emp_type', 'unit_name', 'shift', 'Date', 'accd_type', 'dept', 'emp_name']

        strict = STRICTNESS.RETURN_NO_RESULTS


class ManhoursFilter(django_filters.FilterSet):
    Date = django_filters.DateFromToRangeFilter(widget=RangeWidget())

    class Meta:
        model = Manhours
        fields = ['Date', 'unit_name']

        strict = STRICTNESS.RETURN_NO_RESULTS
