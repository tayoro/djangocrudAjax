from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.forms import TaskForm
from tasks.models import Task
from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import render, redirect
# from django.template import loader


# poster les données dans la base de donnée
def home(request):
        return render(request, "home.html")
