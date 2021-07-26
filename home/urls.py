from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('blogspage', views.blogspage, name='blogspage'),
    path('sheets', views.sheets, name='sheets'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('handlesignup', views.handleSignup, name='handleSignup'),
    path('handlelogin', views.handleLogin, name='handleLogin'),
    path('handlelogout', views.handleLogout, name='handleLogout'),
]
