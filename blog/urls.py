from django.urls import path
# from blog.views import index
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()), # CBV 방식의 call
    # path('', views.index), # FBV 방식의 call
    # path('<int:pk>/', views.single_post_page),
]