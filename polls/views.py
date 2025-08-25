from django.http import HttpResponse
from .models import Article, Memo
#장고 페이지 구성의 핵심
from django.shortcuts import render

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
def memo_list(self) :
    #메모 전체 가져오기
    all_memo = Memo.objects.all()
    #content 구성하기
    content = ""
    for memo in all_memo :
        content += "제목 : " + memo.title + "<br>"
        content += "내용 : " + memo.content + "<br>"
        content += "----" * 10 + "<br>"

    return HttpResponse(content)

#content = "제목 : 타이틀
# 내용 : 콘텐트
# 제목 : 타이틀
# 내용 : 콘텐트
# .
# .
# .
# " enter -> <br>

def one_memo(request, memo_id) :
    memo = Memo.objects.get(id=memo_id)
    content = f"""<h1>제목 : {memo.title}</h1> <br><br>
        내용 : {memo.content} <br>
        {memo.is_important}<br>
        {memo.created_at}
    """
    return HttpResponse(content)

#from django.shortcuts import render 내용 하기, 저거 추가해야 함
#index에서 context 만들어서 보내기
def index(request) :
    memos = Memo.objects.all()
    context = {
        "name" : "lion",
        "title" : "장고 학습",
        "memos" : memos
    }
    return render(request=request, template_name="polls/index.html", context=context)  #경로에서 templatesd 아래부터 적기

def search(request) :
    query = request.GET['q']
    return HttpResponse(f"{query}가 검색되었습니다")