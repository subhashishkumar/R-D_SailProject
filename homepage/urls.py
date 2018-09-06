from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='welcome'),
    path('members', views.MemberPageView.as_view(), name='members'),
]