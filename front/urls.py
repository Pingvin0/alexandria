from django.urls import path
from . import views
app_name = "front"

urlpatterns = [
    path('', views.index, name='index'),
    path('api_keys/', views.api_keys, name='api_keys')
]