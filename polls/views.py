from django.http import HttpResponse
from django.contrib import messages
from .models import Article, Memo
#장고 페이지 구성의 핵심
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
    return HttpResponse("Hello, polls!")

def hello(request):
    """
    가장 간단한 View 함수
    - request: Django가 자동으로 전달하는 요청 정보
    - HttpResponse: 브라우저에 보낼 응답
    """
    return HttpResponse("Hello, Django World!")

def lion(request, name) :
    return HttpResponse(f"""{name}가 장고를 배웁니다!!!""")

def good(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✨ 화려한 페이지 ✨</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');

        body {
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
            color: #fff;
            background: linear-gradient(45deg, #FF6B6B, #556270, #FFD166, #A3A3C7);
            background-size: 400% 400%;
            animation: gradientAnimation 15s ease infinite;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            text-align: center;
            overflow: hidden;
        }

        @keyframes gradientAnimation {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }

        .container {
            position: relative;
            padding: 50px;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(10px);
            animation: fadeInScale 1s ease-in-out;
            border: 2px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.3s ease-in-out;
        }

        .container:hover {
            transform: translateY(-10px) scale(1.05);
        }

        @keyframes fadeInScale {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        h1 {
            font-size: 4em;
            text-transform: uppercase;
            letter-spacing: 5px;
            font-weight: 700;
            margin: 0;
            background: linear-gradient(45deg, #FFD700, #FF69B4, #00BFFF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: sparkle 2s infinite ease-in-out;
        }

        @keyframes sparkle {
            0%, 100% {
                text-shadow: 0 0 10px #FFD700, 0 0 20px #FF69B4, 0 0 30px #00BFFF;
            }
            50% {
                text-shadow: none;
            }
        }

        p {
            font-size: 1.2em;
            margin-top: 20px;
            font-style: italic;
        }

        .button {
            display: inline-block;
            margin-top: 30px;
            padding: 15px 30px;
            background: #fff;
            color: #333;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 700;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease-in-out;
            position: relative;
            overflow: hidden;
        }

        .button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300%;
            height: 300%;
            background: rgba(255, 255, 255, 0.1);
            transform: translate(-50%, -50%) rotate(45deg);
            transition: all 0.5s ease-in-out;
            z-index: 1;
        }

        .button:hover::before {
            width: 0;
            height: 0;
        }

        .button:hover {
            transform: translateY(-5px) scale(1.1);
            background: #E0E0E0;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
        }

        .star {
            position: absolute;
            background-color: #fff;
            border-radius: 50%;
            opacity: 0;
            animation: starfall 10s linear infinite;
        }

        @keyframes starfall {
            0% {
                transform: translateY(-100px) scale(0);
                opacity: 0;
            }
            20% {
                opacity: 1;
            }
            100% {
                transform: translateY(100vh) scale(1);
                opacity: 0;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Welcome!</h1>
        <p>This is a vibrant and animated web page.</p>
        <a href="#" class="button">Explore</a>
    </div>

    <script>
        function createStar() {
            const star = document.createElement('div');
            star.classList.add('star');
            
            const size = Math.random() * 5 + 1;
            star.style.width = size + 'px';
            star.style.height = size + 'px';
            
            star.style.left = Math.random() * 100 + 'vw';
            star.style.animationDuration = Math.random() * 5 + 5 + 's';
            star.style.animationDelay = Math.random() * 2 + 's';
            
            document.body.appendChild(star);

            setTimeout(() => {
                star.remove();
            }, 10000);
        }

        setInterval(createStar, 200);
    </script>

</body>
</html>""")

#view 만들기
#polls에 urls.py 작성
#path("경로", 뷰함수)

#config.urls.py
#path("아무거나경로", include(polls.urls))

#브라우저에서 확인

#각 url로 접근하여 페이지가 나오도록 해보겠습니다.
#1. /polls/hello -> "안녕하세요" 라고 페이지에 표시하기
#2. /polls/good/ -> AI를 통해 작성된 화려한 페이지

#내가 request 라는 객체가 생소한데, 안에 어떤 내용들이 있는지 확인 해 보고 싶어
#이거를 하나의 뷰로 만들어서 웹에 표시해 볼까?
#디버그 하는 역할이네 -> debug_request로 이름짓자
def debug_request(request) :
    #request의 메서드와
    #request의 path
    #request의 META>REMOTE_ADDR를 화면에 표시하자!
    content = """이것이 request가 가지고 있는 정보의 예시입니다. <br>
        request.path = {request.path} <br>
        request.method = {request.method} <br>
        request.META.REMOTE_ADDR = {request.META.get('REMOTE_ADDR', 'Unknown')} <br>
    """
    return HttpResponse(content)

#디버그 버튼 누르시고, launch.json파일 만들기 선택
#엉뚱한 디버그들 선택 해보기
#생성된 launch.json을 삭제하고 다시 장고 디버그 설정으로 수정하기
#디버그 가동
#디버그 뷰에서 브레이크 포인트 잡기

#import 하기
#from .models import Article, Memo 이거 하기
#메모리스트를 보여주는 뷰를 만들어 보겠습니다.
#path('memo/', memo_list)경로 만들어서 화면 틀 확인하기
# def memo_list(self) :
def memo_list(request) :
    #메모 전체 가져오기
    #all_memo = Memo.objects.all()
    #content 구성하기
    # content = ""
    # for memo in all_memo :
    #     content += "제목 : " + memo.title + "<br>"
    #     content += "내용 : " + memo.content + "<br>"
    #     content += "----" * 10 + "<br>"

    # return HttpResponse(content)
    memos = Memo.objects.all().order_by('-created_at')
    context = {
        "memos" : memos
    }
    return render(request, 'polls/memo_list.html', context)

#content = "제목 : 타이틀
# 내용 : 콘텐트
# 제목 : 타이틀
# 내용 : 콘텐트
# .
# .
# .
# " enter -> <br>

def memo_detail(request, pk) :
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'polls/memo_detail.html', {'memo': memo})

#from django.shortcuts import render 내용 하기, 저거 추가해야 함
#index에서 context 만들어서 보내기
def index(request) :
    # memos = Memo.objects.all()
    # context = {
    #     "name" : "lion",
    #     "title" : "장고 학습",
    #     "memos" : memos
    # }
    # return render(request=request, template_name="polls/index.html", context=context)  #경로에서 templatesd 아래부터 적기
    return render(request=request, template_name="polls/index.html")

#디버깅할때 
#아무것도 로그인 정보가 없으면
#from django.contrib.auth.models import User
#User 하면 뭔가 나오고
#User.objects.all()하면 유저 리스트가 나옴
#from polls.models import Memo
#Memo.objects.all() 하면 메모 리스트가 나옴
#1번 아이디의 유저가 쓴 메모리스트를 뽑고싶다면
#user=User.objects.get(pk=1)
#Memo.objects.filter(author=user) 이렇게 하면 리스트 좌라락 나옴
#user.memos.all()하면 걍 전체 메모리스트 뽑을 수 있음 맨 위에처럼 여러번 안해도 됨


def search(request) :
    query = request.GET['q']
    return HttpResponse(f"{query}가 검색되었습니다")

from .forms import MemoModelForm
from django.contrib.auth.decorators import login_required

@login_required
#request.user 이런식으로 유저 로그인 정보 확인 가능 디버깅
def memo_create(request) :
    if request.method == "POST" :
        # 원래는title = request.POST.get['title']
        #  그렇다면 form ??
        # return ??
        form = MemoModelForm(request.POST)
        if form.is_valid() :
            #폼 저장하고 페이지 화면 어떻게 처리할래?
            # 1. 메모 리스트로 가기?
            #form.save()
            #return redirect('polls:memo_list')
            # 2. 지금 작성한 메모를 보여주기? detail
            #memo = form.save()
            #------------------------------------------
            #이제 로그인해야 글 쓰기 기능 할거임
            #직접 입력되지 않는 정보(ex - user)를 추가 입력할때는 form.save(commit=False)를 사용한다!
            memo = form.save(commit=False)  #작가정보 입력됐는지 확인 전에 잠깐 멈추라는 뜻
            memo.author = request.user      #request.user에서 작가정보 가져와서 memo.author에 넣기
            memo.save()
            pk = memo.id
            return redirect('polls:memo_detail', pk=pk) #redirect에는 request를 전달하지 않음
        # 1.form을 이용해서 저장하는 프로세스 체크
        # 2. 페이지 요청할때, 인자를 담아서 보내기
        # 3. 과제 -> memo detail 페이지 기존에 하드코딩된 형태에서 template 이용한 내용으로 변경하기
    else :
        form = MemoModelForm()
        context = {
            'form' : form
        }
        return render(request, 'polls/memo_create.html', context)
    # #디버깅할때는 pass 입력해보기(여기 뿐만 아니라 모두)
    # # step 1
    # # 고객이 입력할 수 있는 화면 보여주기
    # #get으로 요청이 오면, 이거는 주소로 접근하는 거라서, 입력 폼을 보여줍니다
    # if request.method == 'GET' :
    #     return render(request, 'polls/memo_create.html')
    # #post로 요청이 오면, DB에 입력하라는 요청임으로 DB입력 처리를 끝내고, 다른 페이지를 보여줍니다
    # #리턴값 디버깅 입력할때는 get으로 확인할거면 request.GET['title'] 이런 식으로
    # #Memo.Objects.create(title, content) 이게 제대로

    # # step 2
    # # 고객이 입력한 정보를 확인 -> 고객이 입력한 정보 어디있나?
    # # title, content
    # # Memo에 입력
    # # 다음 페이지로 보내기
    # else :
    #     title = request.POST.get('title', 'no_title')  #request.POST['title']
    #     content = request.POST.get('content', 'no_content')
    #     Memo.objects.create(title=title, content=content)
    #     return redirect("polls:memo_list")      #redirect 위에 import에 입력하기


def test1(request) :
    return render(request, 'polls/test1.html')

def test2(request) :
    return render(request, 'polls/test2.html')

# get_object_or_404 임포트하기
#에러메세지 임포트 하기
#from django.contrib import messages
@login_required
def memo_update(request, pk) :
    #수정 화면이 나와야지(GET)
    memo = get_object_or_404(Memo, pk = pk)
    #여기부터는 작성자권한 하기 전 내용
    # if request.method == "GET" :
    #     # memo = Memo.objects.get(pk = pk)
    #     #메모 내용을 가져와서 넣음, create와 다르게 수정해야하니
    #     form = MemoModelForm(instance=memo)
    #     return render(request, 'polls/memo_create.html', {'form' : form})
    # else :
    #     form = MemoModelForm(request.POST, instance=memo)
    #     if form.is_valid() :
    #         form.save()
    #         return redirect('polls:memo_datail', pk=pk)
    if memo.author != request.user :
        messages.error(request, '자신의 메모만 수정할 수 있습니다.')
        return redirect('polls:memo_detail', pk=pk)
    
    if request.method == "POST" :
        form = MemoModelForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            messages.success(request, '메모가 수정되었습니다.')
            return redirect('polls:memo_detail', pk=pk)
    else:
        form = MemoModelForm(instance=memo)
        context = {'form' : form}
        return render(request, 'polls/memo_create.html', context)

@login_required
def memo_delete(request, pk) :
    memo = get_object_or_404(Memo, pk=pk)

    if memo.author != request.user :
        messages.error(request, '자신의 메모만 수정할 수 있습니다.')
        return redirect('polls:memo_detail', pk=pk)

    if request.method == "POST" :
        memo.delete()
        return redirect("polls:memo_list")
    return render(request, 'polls/memo_confirm_delete.html', {"memo" : memo})

# 1. CRUD
# 2. UD에 해당하는 뷰, 템플릿 구성
# 3. 각 템플릿에

@login_required
def my_memo_list(request) :
    #내 메모 인스턴스들 받기
    #context에 담아서 보내기
    memos = Memo.objects.filter(author=request.user).order_by('-created_at')
    #memos = request.objects.user.memos.all()
    context = {
        "memos" : memos
    }
    return render(request, 'polls/my_memo_list.html', context)

from django.db.models import Q
def memo_search(request) :
    #base.url의 검색 영역을 form으로 감싸기
    #polls.urls.py에 검색 url 추가
    #views에 memo_search 작성 준비
    query = request.GET.get('q', "")
    memos = Memo.objects.filter(
        Q(title__icontains = query) | Q(content__icontains = query)
    )
    context = {
        "memos" : memos
    }
    return render(request, 'polls/my_memo_list.html', context)