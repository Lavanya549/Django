from django.urls import path # type: ignore
from app import views
urlpatterns=[
  path('',views.func,name='home'),
  path('wish/<str:name>',views.hbd),
  path('p/<str:name>',views.poem),
  path('index',views.index,name='i'),
  path('navbar',views.navbar,name='t'),
  path('display',views.display,name='d'),
  path('new',views.temp,name='n'),
  path('pro',views.problem),
  path('about',views.about,name='a'),
  path('contact',views.contact,name='c'),
  path('pali/<str:word>',views.palindrome,name="pali"),
  path('display1',views.display1,name='d1'),
  path('laptop',views.laptop,name='lap'),
  path('mobile',views.mobile,name='mob'),
  path('indian1',views.convertion,name="c1"),
  path('book',views.book,name="book")
]