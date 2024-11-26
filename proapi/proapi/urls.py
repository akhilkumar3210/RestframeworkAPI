"""proapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from iapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun1),
    path('f',views.f2),
    path('f3',views.f3),
    path('f4/<d>',views.f4),
    path('f4/<d>',views.f4),
    path('f5',views.f5),
    path('f6/<d>',views.f6),
    path('f7',views.f7.as_view()),
    path('f8/<d>',views.f8.as_view()),
    path('f9',views.genericapiview.as_view()),
    path('f10',views.udpate.as_view()),
    
    
    
    
    
    
    
]
