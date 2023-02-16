from django.urls import path
from . import views


urlpatterns = [
    path('viewlogs', views.viewlogs, name='viewlogs'),
]
