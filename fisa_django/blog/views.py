from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

class PostCreate(CreateView):
    model = Post
    fields = ["title", "content", "head_image"]

    # CreateView가 내장한 함수 - 오버라이딩
    # tag는 참조관계이므로 Tag 테이블에 등록된 태그만 쓸 수 있는 상황
    # 임의로 방문자가 form에 Tag를 달아서 보내도록 form_valid()에 결과를 임시로 담아두고
    # 저장된 포스트로 돌아오도록
    def form_valid(self, form):
        response = super(PostCreate, self).form_vaild(form)
        return super().form_valid(form)

class PostDetail(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = '임의로 작성한 새로운 변수'
        print( context["now"])
        return context

class PostList(ListView):   # post_list.html, post-list
    model = Post
    # template_name = 'blog/index.html'
    # ordering = '-pk'
    context_object_name = 'post_list'

# Create your views here.
def index(request): # 함수를 만들고, 그 함수를 도메인 주소 뒤에 달아서 호출
    posts = Post.objects.all() # 1. 쿼리로 데이터를 모두 가져옵니다
    # 가져온 데이터는 어디에 뿌려야 하나요? Templates로 보내야겠죠
    return render(
        request,
        'blog/index.html',
        {
            'posts':posts, 'my_list': ["apple", "banana", "cherry"], 'my_text': "첫번째 줄 \n 두번째 줄", 'content' : '<img src="data/jjangu.jpg"/>'
        }
    )

def about_me(request): # 함수를 만들고, 그 함수를 도메인 주소 뒤에 달아서 호출
    posts = Post.objects.all() # 1. 쿼리로 데이터를 모두 가져옵니다
    # 가져온 데이터는 어디에 뿌려야 하나요? Templates로 보내야겠죠
    return render(
        request,
        'blog/about_me.html',
    )