from django.contrib import admin
from django.urls import path
from home import views
from sheets import views

urlpatterns = [
    # API to post a comment
    
    path('postcomment', views.postComment, name='postComment'),  
    path('sheetsearch', views.sheetsearch, name='sheetsearch'),  
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.cheatsheetPost, name='cheatsheetPost'),

]
