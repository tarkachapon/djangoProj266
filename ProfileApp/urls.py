"""djangoProj266 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('education/', views.education, name='education'),
    path('interest/', views.interest, name='interest'),
    path('career/', views.career, name='career'),
    path('idol/', views.idol, name='idol'),
]
