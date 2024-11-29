from django.urls import path
from .views import customer_list, home

urlpatterns = [
    path('', home, name='home'),
    path('customers/', customer_list, name='customer_list'),
]



