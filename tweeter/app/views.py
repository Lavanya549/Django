from django.shortcuts import render,redirect
from app.urls import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def register(request):
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
    return redirect('login')
  return render(request,'register.html')

def loginview(request):
  if request.method == "POST":
    uname = request.POST.get("uname")
    pword = request.POST.get("passw")
    obj = authenticate(username=uname, password=pword)
    if obj:
      login(request, obj)
      print(obj)
      return redirect("home")
    return redirect("login")
  return render(request, "login.html")

def navbar(request):
  return render(request,'navbar.html')

def single(request):
  return render(request,'single.html')

def post(request):
  return render(request,'post.html')

def home(request):
  return render(request,'home.html')

def logoutview(request):
  return redirect('login')

def profile(request):
  return render(request,'profile.html')