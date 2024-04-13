from django.urls import path

from food.api.v1.views import FoodsListAPIView

urlpatterns = [
    path('api/v1/foods/', FoodsListAPIView.as_view()),
]
