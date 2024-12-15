from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView, View, DeleteView
from .models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate,logout,login

def index(request):
    program = Programming.objects.all()
    d = {'program': program}
    return render(request,'dropdown/index.html',d)

    
def insert(request):
    #recuperer l'id de champ entrée de programing
                                                        # name = "programming" => voir html
    programming =Programming.objects.get(id=request.POST['programming'])
    #recuperer l'id de champ entrée de courses
    courses = Course.objects.get(id=request.POST['courses'])
    print(programming)
    print(courses)
    member = Member(name=request.POST['name'], programming_id=programming.id, courses_id=courses.id)
    member.save()
    return redirect('/')

# charger Course dependante de Programing
def load_courses(request):
    # recuperer l'id de Programing
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'dropdown/courses_dropdown_list_options.html', {'courses': courses})


