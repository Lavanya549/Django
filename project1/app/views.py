from django.shortcuts import render,redirect
from app.models import *
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def display(request):
  if request.method=="POST":
    m=request.POST.get("movie")
    he=request.POST.get("heroine")
    h=request.POST.get("hero")
    obj=movies(movien=m,heroinen=he,heron=h)
    obj.save()
    result=movies.objects.all()
    return render(request,'form.html',{'res':result,'obj':obj})
  return render(request,'form.html')
  
def display1(request,rid):
  obj= movies.objects.get(id=rid)
  return render(request,'form2.html',{'obj':obj})

def adduser(request):
  if request.method=="POST":
    u=request.POST.get('uname')
    f=request.POST.get('fname')
    l=request.POST.get('lname')
    m=request.POST.get('mail')
    p=request.POST.get('passw')
    print(u,f,l,m,p)
    if User.objects.filter(username=u).exists():
      d={'warn':"User is already exists"}
      return render(request,'register.html',d)
    if len(u)<6:
      d={'warn':"username length is small"}
      return render(request,'register.html',d)
    if p.isalnum():
      d={'warn':"password doesnt contain any special characters"}
      return render(request,'register.html',d)   
    if len(p)<8:
      d={'warn':"password length is too short....!"}
      return render(request,'register.html',d)
    obj=User.objects.create_user(
      username=u,
      first_name=f,
      last_name=l,
      email=m,
      password=p
    )
    obj.save()
    return render(request,'register.html')
  return render(request,'register.html')



