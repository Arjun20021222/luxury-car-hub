import django_filters
from showroom.models import Car

class CarFilter(django_filters.FilterSet):
    min_price=django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gte"
    )

    max_price=django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte"
    )

    min_year = django_filters.NumberFilter(
        field_name="year",
        lookup_expr="gte"
    )

    max_year = django_filters.NumberFilter(
        field_name="year",
        lookup_expr="lte"
    )

    class Meta:
        model = Car

        fields = [
            "brand",
            "color",
            "fuel_type",
            "transmission",
            "available",
        ]
