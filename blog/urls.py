from django.contrib import admin
from django.urls import path
from home import views
from blog import views

urlpatterns = [
    # API to post a comment
       
    path('blogpostcomment', views.blogpostComment, name='blogpostComment'),  
    path('blogsearch', views.blogsearch, name='blogsearch'),    
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),

]
