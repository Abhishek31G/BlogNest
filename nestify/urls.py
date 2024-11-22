from django.urls import path
from nestify.views import *
from django.contrib.auth import views as auth_views

        
urlpatterns = [
    # Authentication Url's
    path('signup/', handleSignup, name="signup"),
    path('login/', handleLogin, name="login"),
    path('logout/', handleLogout, name="logout"),


    # General Url's
    path('', home, name="home"),
    path('post/<int:pk>', post_detail, name="post_detail"),
    path('post/new', create_post, name="create_post"),
    path('post/edit/<int:pk>', edit_post, name="edit_post"),
    path('post/delete/<int:pk>', delete_post, name="delete_post"),
]