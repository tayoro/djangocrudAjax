from django.urls import path
from .views import TaskView, ViewTaskView, TaskUpdateDeleteView,TutorialDataView, TutorialView #, TutorialDataView, TaskUpdateView

app_name = "tasks"

urlpatterns = [
    path('', TaskView.as_view(), name="task"), 
    path('view', ViewTaskView.as_view(), name="view"), 
    path('view/<int:pk>', TaskUpdateDeleteView.as_view(), name="updateDelete"), 
    #path('view/<int:pk>', TaskUpdateView.as_view(), name="update"),
    
    path('tutorial', TutorialView.as_view(), name="tutorial"),
    path('tutorial/data', TutorialDataView.as_view(), name="tutorial_data"), 
    
    
]