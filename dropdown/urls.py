from django.urls import path
from .views import index, load_courses, insert

app_name = "dropdown"

urlpatterns = [
    path('', index, name="index"), 
    path('insert/', insert, name='insert'),
    path('load-courses/', load_courses, name='ajax_load_courses'),
]