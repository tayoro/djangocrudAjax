from django.db import models

# Create your models here.

class Programming(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    programming = models.ForeignKey(Programming, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=30, blank=True)
    programming = models.ForeignKey(Programming, blank=True, null=True, on_delete=models.CASCADE)
    courses = models.ForeignKey(Course, blank=True, null=True ,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
        