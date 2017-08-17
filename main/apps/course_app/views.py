from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    context = {
        "courses": Course.objects.all().values()
    }
    return render(request,'course_app/index.html', context)
def create(request):
    Course.objects.create(name=request.POST["title"])
    return redirect("/")

def delete(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request,'course_app/destroy.html', context)

def process_destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect("/")

def keep_record(request):
    return redirect("/")
