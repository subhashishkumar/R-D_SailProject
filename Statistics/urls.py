from django.urls import path
from . import views

urlpatterns = [
    path('Statistics/home', views.first_page.as_view(), name='Statistics'),
    path('Statistics/FatalDataView/', views.fatal, name='FatalDataView'),
    path('Statistics/FatalPieDataView/', views.fatal_pie, name='FatalPieDataView'),
    path('Statistics/CauseDataView/', views.cause, name='CauseDataView'),
    path('Statistics/ManhoursDataView/', views.manhours, name='ManhoursDataView'),

    
]