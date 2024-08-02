from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Includes routes from api/urls.py
    path('', home_view, name='home'),
]
