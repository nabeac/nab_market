from django.urls import path, include
from .views import home, vue_product, category
urlpatterns = [
    path('', home, name='home'),
    path('vue/<int:pk>', vue_product, name='vue'),
    path('category/<str:cat>', category, name='category'),
    path('blog', include('blog.urls')),
    path('cart/', include('cart.urls')),
]