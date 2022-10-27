from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class PostList(ListView):
  model = Post
  # template_name = 'blog/index.html'

class PostDetail(DetailView):
  model = Post

# 샘플
# def index(request):
#     # 필요한 코드 넣기
#     datas ="블로그 데이터"
#     # render(request, '템플릿파일', {'키':변수값})
#     return render(request, 'blog/index.html', {'datas' : datas})

# blog list up
# def index(request):
#   posts = Post.objects.all().order_by('-pk')

#   return render(
#     request,
#     'blog/index.html',
#     {
#         'posts': posts,
#     }
#   )


# 하나의 post 상세 페이지
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )