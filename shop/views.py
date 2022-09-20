
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
from django.views.generic.base import View
from django.db.models import Q

from cart.forms import CartAddProductForm,CartAddForm

from .models import Category, Product


def index(request):
    add = CartAddForm()
    products = Product.objects.all()
    context = {"title": "Bienvenue chez vous", "products": products,"add":add }    
    
    return render(request, "index.html", context)



class ProductList(View):
    template_name = 'shop/product_list.html'
   
    def get(self, request,category=None):
        
        products = Product.objects.all()
        #je recupere tout les categoris
        categories = Category.objects.all()   
        # si categorie existe 
        if category:
            # Essaye de recuperer la categorie , si la categorie n'existe pas envoyer une exeption
            category = get_object_or_404(Category, slug=category)
            # je filtre sur les products ,
            # le 1er category appartient a la table et la 
            # 2e c'est la categorie passer sur le parametre
            products = products.filter(category=category)


        q = request.GET.get("q")
        request.session["nom"] = "DialloShop"
        request.session.get("nom")
        del request.session["nom"]
        if q:
            products = Product.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(category__name__icontains=q)
            )
        return render(request, self.template_name, 
                      {"products": products, "categories": categories,"category":category  })



class ProductDetail(DetailView):
    model = Product
    context_object_nme = 'product'
    template_name = 'shop/product_details.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context["cart_product_form"] = CartAddProductForm()
        return context

