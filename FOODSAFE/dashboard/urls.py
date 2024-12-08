
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path("", views.home_func, name= "home_func"),
        path("neu/", views.neutritionist_func, name= "neutritionist_func"),
        path("seedreq/", views.seed_request_func, name="seedreq"),
        path("sellpage/",views.seller_func, name= "sellpage"),
        
]   
