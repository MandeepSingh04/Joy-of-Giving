"""hello URL Configuration

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
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("profile", views.profile, name='profile'),
    path("userprofile/<int:pk>", views.userprofile, name='userprofile'),
    path("post", views.createpost, name='post'),
    path("mypost/<int:pk>", views.mypost, name='mypost'),
    path("edit_post/<int:pk>", views.edit_post, name='edit_post'),
    path("login", views.userlogin, name='login'),
    path("signup", views.usersignup, name='signup'),
    path("signupinfo", views.handlesignup, name='signupinfo'),
    path("logininfo", views.handlelogin, name='logininfo'),
    path("logout", views.handlelogout, name='handlelogout'),
    path("mypost/<id>/deletepost", views.deletepost, name='deletepost')
]