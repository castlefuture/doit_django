from django.urls import path
from blog.views import index
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]