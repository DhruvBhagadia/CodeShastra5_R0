"""CodeShastra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app.views import index, linechart, get_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('get_news/', get_news, name="get_news"),
    path('chart/', chart, name="linechart"),
    path('trying/', trying, name="trying"),
    path('sports/', render_sports_page, name="render_sports_page"),
    path('politics/', render_politics_page, name="render_politics_page"),
]
