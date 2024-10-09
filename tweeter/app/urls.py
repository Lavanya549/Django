from django.urls import path
from app import views

urlpatterns=[
  path('',views.home,name="home"),
  path('login',views.loginview,name='login'),
  path('logout',views.logoutview,name='logout'),
  path('register',views.register,name='register'),
  path('post',views.post,name='post'),
  path('single',views.single,name="single"),
  path('profile',views.profile,name="profile")
]