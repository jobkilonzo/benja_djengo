from django.contrib import admin
from django.urls import path, include

from products.views import ProductsListView
from search.views import ProductsSearchView
from django.conf.urls import url


urlpatterns = [
    path('products/', include("products.urls", namespace='products')),
    path('search/', include("search.urls", namespace='search')),
    path('admin/', admin.site.urls),
]
