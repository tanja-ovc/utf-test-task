from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.api.v1.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
