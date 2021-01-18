"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from articles.views import article_full_view, article_list_View
from homepage.views import homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/<slug:date>/<slug:slug>', article_full_view, name='articles'),
    path('', homepage_view),
    path('<int:instrumentId>/articles/', article_list_View, name='articleByInstrument')
]
