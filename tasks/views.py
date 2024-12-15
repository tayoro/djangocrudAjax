from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.forms import TaskForm
from tasks.models import Task
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.template import loader
import json
# from django.shortcuts import render, redirect
# from django.template import loader


# poster les données dans la base de donnée
class TaskView(View):
    # apres validation de la methode ajax (voir si formulaire correcte )
    
    #alors
    form_class = TaskForm
    def post(self, request, *args, **kwargs):
        # si mrethode ajax est validé avec succès
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # au lieu de is_ajax()
            # alors recupere le formulaire avec les données
            form = self.form_class(request.POST)
            # si formulaire valide
            if form.is_valid():
                # save dans la base de données
                form.save()
                return JsonResponse({"message": "success"}) # success voir ajax
            return JsonResponse({"message": "Validation failed"})
        return JsonResponse({"message": "Wrong request"})

    def get(self,request, *args, **kwargs):
        return render(request, "tasks/index.html", {})


class ViewTaskView(View):
    def get(self,request, *args, **kwargs):
        tasks = Task.objects.all()
        return render(request, "tasks/view.html", {"tasks":tasks})



class TaskUpdateDeleteView(View):
    
    # get pour recuperation et supprimer 
    def get(self,request, pk, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # au lieu de is_ajax()
            task = Task.objects.get(pk=pk)
            print(task)
            task.delete()
            return JsonResponse({"message":"success"})
        return JsonResponse({"message": "Wrong request"})
    
    # poster pour Update
    form_class = TaskForm
    def post(self, request, pk, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # au lieu de is_ajax()
            task = Task.objects.get(pk=pk)
            
            # dictionnaire pour transferer dans les pages HTML
            data = {
                "owner":task.owner, 
                "name":task.name, 
                "task_date":task.task_date, 
                "start_time":task.start_time, 
                "end_time":task.end_time
            }
            form = self.form_class(request.POST, initial=data)
            if form.is_valid():
                #(1) affecter a des variables les données recupéré par
                # chaque entrée du formulaire 
                owner = form.cleaned_data['owner']
                name = form.cleaned_data['name']
                task_date = form.cleaned_data['task_date']
                start_time = form.cleaned_data['start_time']
                end_time = form.cleaned_data['end_time']
                
                #(2) si les données du form a changer
                if form.has_changed():
                    # les nouvelle valeurs sont reafectés
                    task.owner = owner
                    task.name = name
                    task.task_date = task_date
                    task.start_time = start_time
                    task.end_time = end_time
                    task.save()
                    return JsonResponse({'message':'success'})
                return JsonResponse({'message': 'Data is not editted'})
            
            return JsonResponse({'message': 'Validation failed'})
        
        return JsonResponse({'message': 'wrong request'})
    
# class TaskUpdateView(View):
#     form_class = TaskForm
    
#     def post(self, request, pk, *args, **kwargs):
#         if request.headers.get('x-requested-with') == 'XMLHttpRequest': # au lieu de is_ajax()
#             task = Task.objects.get(pk=pk)
#             data = {
#                 "owner":task.owner, 
#                 "name":task.name, 
#                 "task_date":task.task_date, 
#                 "start_time":task.start_time, 
#                 "end_time":task.end_time
#             }
#             form = self.form_class(request.POST, initial=data)
#             if form.is_valid():
#                 owner = form.cleaned_data['owner']
#                 name = form.cleaned_data['name']
#                 task_date = form.cleaned_data['task_date']
#                 start_time = form.cleaned_data['start_time']
#                 end_time = form.cleaned_data['end_time']
                
#                 if form.has_changed():
#                     task.owner = owner
#                     task.name = name
#                     task.task_date = task_date
#                     task.start_time = start_time
#                     task.end_time = end_time
#                     task.save()
#                     return JsonResponse({'message':'success'})
#                 return JsonResponse({'message': 'Data is not editted'})
            
#             return JsonResponse({'message': 'Validation failed'})
        
#         return JsonResponse({'message': 'wrong request'})
                
class TutorialView(View):
    def get(self,request, *args, **kwargs):
            # tasks = Task.objects.all()
            # # seralise les donnée 
            # task_serializers = serializers.serialize('json', tasks)
            # # convertir en objet Json
            # task_json = json.loads(task_serializers)
            # context = {'task_json': task_json}
            # print(task_json)
            # return render(request, "tasks/tutorial.html", context)
            return render(request, "tasks/tutorial.html")
    
    
class TutorialDataView(View):
    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # au lieu de is_ajax()
            tasks = Task.objects.all()
            # seralise les donnée
            task_serializers = serializers.serialize('json', tasks)
            # convertir en objet Json
            task_json = json.loads(task_serializers)
            return JsonResponse(task_json, safe=False)
        return JsonResponse({'message':'wrong validation'})
    


    
    
            