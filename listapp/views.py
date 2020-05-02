from django.shortcuts import render,redirect
from.models import Task
from. forms import *
# Create your views here.
def home(request):
    task=Task.objects.all()
    form = TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, "listapp/home.html",{"task":task,"form":form})

def update(request,pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == "POST":
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,"listapp/update.html",{"form":form})
def delete(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request, "listapp/delete.html", {"item": item})