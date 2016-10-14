from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from mysite.member.models import MyUser
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        try:
            email= request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']
            nickname = request.POST['nickname']
        except KeyError:
            return HttpResponse('입력해주세요')

        if password1 != password2:
            return HttpResponse('패스워드가 일치하지 않습니다.')

        user = MyUser.objects.create_user(
            # 내가생성한 UserManager와 일치하게 작성
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname,
            password=password1,
        )

        auth_login(request, user)
        return redirect('blog:post_list')
    else:
        return render(request, 'member/signup.html')

