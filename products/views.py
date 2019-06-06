from django.views.generic import ListView

from .models import Products

class ProductsListView(ListView):
    queryset = Products.objects.all()
    template_name = "products/list.html"
