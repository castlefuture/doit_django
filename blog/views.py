from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag

# Create your views here.

def tag_page(request, slug):
  tag = Tag.objects.get(slug=slug)
  post_list = tag.post_set.all()

  return render(
    request,
    'blog/post_list.html',
    {
      'post_list': post_list,
      'tag' : tag
      'categories': Category.objects.all(),
      'no_category_post_count': Post.objects.filter(category=None).count(),
    }
  )


class PostList(ListView):
  model = Post
  ordering= '-pk'

def get_context_data(self, **kwargs):
  context = super(PostList, self).get_context_data()
  context['categories'] = Category.objects.all()
  context['no_category_post_count'] = Post.objects.filter(category=None).count()
  return context

def category_page(request, slug):
  if slug == 'no_category':
    category = '미분류'
    post_list = Post.objects.filter(category=None)
  else:
    category = Category.objects.get(slug=slug)

  return render(
    request,
    'blog/post_list.html',
    {
      'post_list': post_list,
      'categories': Category.objects.all(),
      'no_category_post_count': Post.objects.filter(category=None).count(),
      'category': category,
    }
  )

  # template_name = 'blog/index.html'

class PostDetail(DetailView):
  model = Post


class PostDetail(DetailView):
  model = Post

  def get_context_data(self, **kwargs):
    context = super(PostDetail, self).get_context_data()
    context['categories'] = Category.objects.all()
    context['no_category_post_count'] = Post.objects.filter(category=None).count()
    return context

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