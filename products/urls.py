from django.urls import path
from products.views import ProductView, ProductCategoryView, FormRegisterView

app_name = "products"

urlpatterns = [
    path('', ProductView.as_view(), name="products"), 
    path('register', FormRegisterView.as_view(), name="register"),
    path('<str:category>', ProductCategoryView.as_view(), name="products_category"), 
]