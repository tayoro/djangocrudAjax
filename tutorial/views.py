from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django.template import loader
from products.models import Product
from tutorial.models import Tuto



class TutorialView(View):
    def post(self,request, *args, **kwargs):
        tuto = Tuto(product=request.POST.get('product'), category=request.POST.get('category'))
        tuto.save()
        return redirect('/')
            
    def get(self,request, *args, **kwargs):
        products = Product.objects.values('category').distinct()
        context = {
            "product_list": products
        }
        return render(request, "tutorial/index.html", context)
    
# charger les produits dependant de category
class GetProductView(View):
    def get(self,request, category, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # au lieu de is_ajax()
            products = Product.objects.filter(category=category).values('id', 'name')
            return JsonResponse({'data': list(products)})
        return HttpResponse('Wrong request')
    
    

 
    
