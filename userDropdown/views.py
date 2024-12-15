from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django import http
from .models import Student, Branch
from .forms import StudentForm
from django.shortcuts import render

class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
                                  # app-name:pattern-name
    success_url = reverse_lazy('userDropdown:student_changelist')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm  
                                  # app-name:pattern-name
    success_url = reverse_lazy('userDropdown:student_changelist')
    
class StudentDeleteView(DeleteView):
    model = Student
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('userDropdown:student_changelist')
    template_name = 'userDropdown/confirm-delete.html'
    

def load_branches(request):
    college_id = request.GET.get('college')
    branches = Branch.objects.filter(college_id=college_id).order_by('name')
    return render(request, 'userDropdown/branch_dropdown_list_options.html', {'branches': branches})
