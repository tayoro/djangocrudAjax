from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django.template import loader
from products.models import Product



class ProductView(View):
    def get(self,request, *args, **kwargs):
        products = Product.objects.values('category').distinct()
        context = {
            "product_list": products
        }
        return render(request, "products/index.html", context)
    

class ProductCategoryView(View):
    def get(self,request, category, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # au lieu de is_ajax()
            products = Product.objects.filter(category=category)
            context = {
                "product_image_list": products
            }
            template = loader.get_template("products/category.html")
            return HttpResponse(template.render(context, self.request))
        return HttpResponse("Wrong request")
    
    
class FormRegisterView(View):
    def post(self,request, *args, **kwargs):
        tuto = Product(name=request.POST.get('name'), category=request.POST.get('category'), image=request.POST.get('file'), created_at=request.POST.get('created_at'), updated_at=request.POST.get('updated_at'))
        tuto.save()
        return redirect('/')
    
    def get(self, request, *args, **kwargs):
        return render(request, "products/formulaire.html", {})

    