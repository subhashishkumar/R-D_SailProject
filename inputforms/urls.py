from django.urls import path
from inputforms import views

urlpatterns = [
    path('accdform/', views.AccdView.as_view(), name='AccdForm'),
    path('manhoursform/', views.ManhoursView.as_view(), name='ManhoursForm'),
]
