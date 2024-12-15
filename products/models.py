from django.db import models

class Product(models.Model):
    name = models.CharField(null=True, blank=True, max_length = 150)
    category = models.CharField(null=True, blank=True, max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="products")
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, auto_now=True)
    
    def __str__(self):
        return f"{self.name}"