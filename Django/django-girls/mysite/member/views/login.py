from django.http import HttpResponse
from django.contrib.auth import authenticate as auth_authenticate,\
    login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages

def login(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        for item in request.session.items():
            print(item)
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            return HttpResponse('username 또는 password는 필수항목입니다')
        user = auth_authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            # 이때 session-id생성
            # 이름과 달리 실제로 인증 과정 마무리 단계 담당
            # 이 함수를 통해 session 정보를 만들지않으면 다른 페이지 방문할때마다 매번로그인해야한다.
            messages.success(request, '로그인에 성공하였습니다')
            return redirect(next)
        else:
            messages.error(request, '로그인에 실패하였습니다')
            # context = {
            #     'error_message': '로그인에 실패하였습니다'
            # }
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})
