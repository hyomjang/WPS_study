from django.shortcuts import render, render_to_response
from .models import Post

# Create your views here.

# post_list 라는 이름의 view
# Post인스턴스를 전부 가져와 posts 라는 이름으로 'post_list.html' 탬플릿에 전달해준다
def post_list(request):
    # ORM을 이용해서 Post인스턴스를 전부 가져옵니다
    posts = Post.objects.all()

    # 탬플릿에 전달할 dictionary 객체
    ret = {
        'title' : '블로그 글 목록',
        'posts' : posts
    }
    return render_to_response('Post_list.html', ret)