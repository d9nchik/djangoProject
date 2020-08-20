"""djangoProject URL Configuration

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
from django.urls import path, re_path
from movies.views import MovieView
from candies.views import MainPageView, CandyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieView.as_view()),
    path("candies/", MainPageView.as_view()),
    re_path("candies/(?P<candy_name>[^/]*)/?", CandyView.as_view()),
]
