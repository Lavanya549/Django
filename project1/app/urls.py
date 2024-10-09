
from django.urls import path
from app import views

urlpatterns=[
  path("",views.display,name='b'),
  path("movies/<int:rid>",views.display1,name="a"),
  path('register',views.adduser,name='r'),
]
