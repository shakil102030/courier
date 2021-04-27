from django.urls import path
from .views import OrderView, OrderTable

urlpatterns = [
    path('', OrderView, name = 'OrderView'),
    path('table/', OrderTable, name = 'OrderTable'),
    
   
]