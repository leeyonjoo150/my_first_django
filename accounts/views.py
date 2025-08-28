from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request) :
    if request.method == "POST" :
        #디버깅 할때 request.user     request.GET    request.POST 이런 식으로 가능
        username = request.POST["username"]
        password = request.POST["password"]

        #인증, 정보가 있으면 리턴, 없으면 안나옴
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            messages.success(request, "로그인 성공")
            return redirect('polls:index')
        else :
            messages.error(request, "아이디나 패스워드가 올바르지 않습니다.")
            #일단은 이대로 두고 수정하자
            return redirect('polls:index')
    else :
        return render(request, 'accounts/login.html')

def logout_view(request) :
    username = request.user.username
    logout(request)
    messages.info(request, f'{username}님 로그아웃되었습니다.')

    return redirect('polls:index')

def signup_view(request) :
    """회원가입 처리 함수형 뷰"""
    if request.user.is_authenticated:
        return redirect('polls:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # 유효성 검사
        errors = []

        if not username or not password1:
            errors.append('아이디와 비밀번호는 필수입니다.')

        if password1 != password2:
            errors.append('비밀번호가 일치하지 않습니다.')

        if len(password1) < 8:
            errors.append('비밀번호는 8자 이상이어야 합니다.')

        if User.objects.filter(username=username).exists():
            errors.append('이미 사용중인 아이디입니다.')

        if errors:
            for error in errors:
                messages.error(request, error)
        else:
            try:
                # 사용자 생성
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1
                )

                # 자동 로그인
                login(request, user)
                messages.success(request, f'{user.username}님 가입을 환영합니다!')
                return redirect('polls:index')

            except IntegrityError:
                messages.error(request, '회원가입 중 오류가 발생했습니다.')

    return render(request, 'accounts/signup.html')