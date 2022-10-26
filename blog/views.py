from django.shortcuts import render
from .models import Post

# Create your views here.
# 샘플
# def index(request):
#     # 필요한 코드 넣기
#     datas ="블로그 데이터"
#     # render(request, '템플릿파일', {'키':변수값})
#     return render(request, 'blog/index.html', {'datas' : datas})

def index(request):
  posts = Post.objects.all().order_by('-pk')

  return render(
    request,
    'blog/index.html',
    {
        'posts': posts,
    }
  )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )