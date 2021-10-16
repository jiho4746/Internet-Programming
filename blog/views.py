from django.shortcuts import render
from django.views.generic import ListView, DetailView
#models와 다른 파일이기 때문에 Post 사용하려면 import!!
from blog.models import Post

# <CBV 스타일로 페이지 만들기>
#블로그 목록
#post_list.html
class PostList(ListView) :
    model = Post
    ordering = '-pk'
#   template_name = 'blog/post_list.html'

#블로그 상세 페이지
#post_detail.html
class PostDetail(DetailView) :
    model = Post





#<FBV 스타일로 페이지 만들기>

#index 함수 - template안 html 파일과 연결
#def index(request) :
#   posts = Post.objects.all().order_by('-pk')

#   return render(request, 'blog/post_list.html',
#                 {
#                     #post도 같이 전달
#                     'posts' : posts
#                 })

#single_post_page 함수 - template안 html 파일과 연결
#def single_post_page(request, pk) :
   #특정 페이지만 가지고 옴
#   post = Post.objects.get(pk=pk)

#   return render(request, 'blog/post_detail.html',
#                 {
#                     'post': post
#                 })