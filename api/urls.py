from django.urls import path
from .views import srm_post, srm_get

urlpatterns = [
    path('srm', srm_post, name='srm_post'),
    path('srm', srm_get, name='srm_get'),
]

