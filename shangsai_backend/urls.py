"""
URL configuration for shangsai_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import HttpResponse
# from django.contrib import admin
from django.urls import path

from Course.views import get_all_courses_view


def index(request):
    return HttpResponse('Hello world1111')
urlpatterns = [
    #    path("admin/", admin.site.urls),
    path('', index),
    path('api/course/get_all_courses',get_all_courses_view),
]
