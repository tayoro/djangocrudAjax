from django.db import models

class Tuto(models.Model):
    product = models.CharField(null=True, blank=True, max_length=150 )
    category = models.CharField(null=True, blank=True, max_length=50)
    
    def __str__(self):
        return f"{self.category}"
    
    
