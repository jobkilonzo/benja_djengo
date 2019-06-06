from django.urls import path
from django.conf.urls import url
from .views import ProductsListView
app_name = "products"
urlpatterns = [
    path('', ProductsListView.as_view(), name="list"),

]
