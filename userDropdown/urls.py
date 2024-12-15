from django.urls import include, path
from . import views

app_name = "userDropdown"

urlpatterns = [
                                                   # pattern-name
    path('', views.StudentListView.as_view(), name='student_changelist'),
    path('add/', views.StudentCreateView.as_view(), name='student_add'),
    path('edit/<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
   ]