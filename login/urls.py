from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logged_out_user, name='logged_out_user'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', views.CustomPasswordChangeDoneView.as_view(), name='password_updated'),
]
