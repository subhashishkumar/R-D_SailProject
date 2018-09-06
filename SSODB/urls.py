"""SSODB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.urls import path, include
from outputviews import views

AdminSite.site_title = ('SSO Administration')
AdminSite.site_header = ('SSO Administration')
AdminSite.index_title = ('SSO Administration')
AdminSite.login_template = 'registration/admin_login.html'
AdminSite.logout_template = 'registration/logout.html'
AdminSite.site_url = None


urlpatterns = [
    path('', include('homepage.urls')),
    path('users/', include('login.urls')),
    path('forms/', include('inputforms.urls')),
    path('output/', include('outputviews.urls')),
    path('Statistics/', include('Statistics.urls')),
    path('admin/', admin.site.urls),
    path('get_unitname/', views.get_unitname, name='get_unitname'),
    path('get_department/', views.get_department, name='get_department'),
]
