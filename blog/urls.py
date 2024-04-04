from django.urls import path
from .views import post_list, post_view
urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>', post_view, name='post'),
]