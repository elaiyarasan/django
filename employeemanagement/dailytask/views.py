from django.http import HttpResponse
from django.shortcuts import render
from .models import Dailytask
from .forms import DailytaskForm
# Create your views here.
def task_management(request):
    task_management=DailytaskForm()
    if request.method=="POST":
        task_management=DailytaskForm(request.POST)
    if task_management.is_valid():
            print(task_management.cleaned_data)
            Dailytask.objects.create(**task_management.cleaned_data)        
    else:
         print(task_management.errors) 
    return render(request,"dailytask/dailytask.html",{"form":task_management})