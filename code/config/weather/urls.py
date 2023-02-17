from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_home_view, name='get_home_view'),
]
