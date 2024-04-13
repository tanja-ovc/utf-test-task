from django.contrib import admin

from food.models import Food, FoodCategory


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'category', 'is_publish')


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru')
