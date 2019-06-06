from django.contrib import admin
from django.urls import path, include

from search.views import ProductsSearchView
from django.conf.urls import url

app_name = "search"

urlpatterns = [
    path('', ProductsSearchView.as_view(), name='query'),
]
