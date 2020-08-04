from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


def courses(request):
    context={
        'all_courses': Course.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        return redirect('/')
    return redirect('/')




def destroy(request, id):
    context={
        'viewed_course': Course.objects.get(id=id)
    }
    
    return render(request, 'one_course.html', context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')