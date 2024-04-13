from django.db.models import Count, Prefetch, Q
from rest_framework import generics

from food.api.v1.serializers import FoodListSerializer
from food.models import Food, FoodCategory


class FoodsListAPIView(generics.ListAPIView):

    queryset = FoodCategory.objects.prefetch_related(
        Prefetch('food',
                 queryset=Food.objects.prefetch_related(
                     'additional'
                 ).filter(is_publish=True))
    ).annotate(
        published_foods_count=Count('food', filter=Q(food__is_publish=True))
    ).filter(published_foods_count__gt=0)

    serializer_class = FoodListSerializer
