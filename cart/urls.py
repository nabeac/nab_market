from django.urls import path, include
from .views import *
urlpatterns = [
    path('', cart, name='cart'),
    path('add/', cart_add, name='cart_add'),
    path('del/', cart_del, name='cart_del'),
    path('update/', cart_up, name='cart_up'),
 ]