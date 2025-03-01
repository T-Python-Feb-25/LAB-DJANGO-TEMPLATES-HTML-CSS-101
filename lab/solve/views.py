from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.

def main(request:HttpRequest):
    return render(request,"solve/main.html")
def task1(request:HttpRequest):
    return render(request,"solve/task1.html")
def task2(request:HttpRequest):
    return render(request,"solve/task2.html")
def task3(request:HttpRequest):
    return render(request, "solve/task3.html")
def cv(request:HttpRequest):
    return render(request,"solve/cv.html")