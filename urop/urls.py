"""urop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path  # For django versions from 2.0 and up
from django.contrib import admin
from allauth.account import views as allauth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^database/', include('database.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
]
urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
import debug_toolbar
urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),

    # For django versions before 2.0:
    # url(r'^__debug__/', include(debug_toolbar.urls)),

] + urlpatterns