from django.shortcuts import render,redirect # type: ignore
from django.http import HttpResponse  # type: ignore
from app.models import bookitem
def func(request):
  return HttpResponse('we are in func1')

def hbd(request,name):
  return HttpResponse(f'HAPPY BIRTHDAY {name}')

def poem(request,name):
  return HttpResponse(f'DADDY:{name} {name}!!<br>{name}:YES,PAPA,<br>daddy:eating sugar?<br>{name}:No papa<br>daddy:telling lies')

def index(request):
  return render(request,'index.html')

def about(request):
  return render(request,'about.html')

def contact(request):
  return render(request,'contact.html')

def navbar(request):
  return render(request,'navbar.html')

def temp(request):
  return render(request,'new.html')

def display(request):
  listofstudents=[
    ['lavanya','CSE',0],
    ['KUSUMA','CSM',10],
    ['harshika','cse',20],

  ]
  context={'data':listofstudents}
  return render(request,'table.html',context)

def display1(request):
  listofstudents=[
    ['lavanya','CSE',0],
    ['KUSUMA','CSM',10],
    ['harshika','cse',20],
    
  ]
  context={'data':listofstudents}
  return render(request,'table2.html',context)  

def problem(request):
  a=int(request.GET.get('num1'))
  b=int(request.GET.get('num2'))
  if a>b:
    return HttpResponse(f'{a} is greater than {b}')
  else:
    return HttpResponse(f'{a} is greater than {b}')
  
def palindrome(request,word):
  result1 = word == word[::-1]
  context={'result2':word,'result':result1}
  return render(request,'palindrome.html',context)

list1=[
    {'id':1,'name':'redmi','ram':'4gb','prize':20000},
    {'id':2,'name':'poco','ram':'8gb','prize':10000},
    {'id':3,'name':'lenovo','ram':'8gb','prize':30000}
  ]

def mobile(request):
  context={'data':list1}
  return render(request,'mobile.html',context)

list2=[
    {'name':'dell','ram':'8gb','prize':100000},
    {'name':'hp','ram':'16gb','prize':20000},
    {'name':'lenovo','ram':'8gb','prize':15000}
  ]

def laptop(request):
  context={'data':list2}
  return render(request,'laptop.html',context)

def convertion(request):
  if request.method == "POST":
    res=request.POST.get('num1')
    d={
      'data':int(res)/84
    }
    return render(request,'indian.html',d)
  return render(request,'indian.html')
 

def book(request):
  result=bookitem.objects.all()[::-1]
  if request.method=="POST":
    bname=request.POST.get("name")
    page=request.POST.get("pg")
    prize=request.POST.get("pc")
    obj=bookitem(name=bname,pages=page,price=prize) # type: ignore
    obj.save()
    return render(request,'forms3.html',{'res':result,'obj':obj})
  return render(request,'forms3.html')