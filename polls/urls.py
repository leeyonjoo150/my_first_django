from django.urls import path
#원하는 뷰를 가져오는 형태
from .views import index, hello, lion, good, debug_request, memo_list, one_memo
#이렇게도 가능
#from polls import index, hello, lion, good, debug_request


urlpatterns = [
    path("index", index),
    path("hello/", hello),
    path("lion/<str:name>/", lion),     #lion 함수 매개변수에 name 추가
    path("good/", good),
    #path("debug/", debug_request)
    path("", debug_request),
    path("memo/", memo_list),    #메모리스트 틀 확인용
    path("memo/<int:memo_id>", one_memo)    #int 뒤의 memo_id는 view의 one_memo(memo_id)의 매개변수와 같아야함
]

#이렇게 해도 됨, 마음에 드는 방식대로 하면 됨
# from . import views

# urlpatterns = [
#     path("hello/", views.hello),
#     path("lion/", views.lion),
#     path("good/", views.good)
#     path("debug/", views.debug_request)
# ]

#url이 어떻게 뷰로 연결되는지 원리를 이해