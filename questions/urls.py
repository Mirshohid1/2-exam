from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions, name='questions'),
    path('questions-all/', views.questions_all, name='questions-all')
]