from django.urls import path
#원하는 뷰를 가져오는 형태
from .views import index, hello, lion, good, debug_request, memo_list, memo_detail, index, search, memo_create, test1, test2
from .views import memo_update, memo_delete, my_memo_list, memo_search
#이렇게도 가능
#from polls import index, hello, lion, good, debug_request

app_name = 'polls'


urlpatterns = [
    # path("index", index),
    path("hello/", hello),
    path("lion/<str:name>/", lion),     #lion 함수 매개변수에 name 추가
    path("good/", good),
    #path("debug/", debug_request)
    #path("", debug_request),
    path("memo/", memo_list, name='memo_list'),    #메모리스트 틀 확인용
    path("memo/<int:pk>", memo_detail, name="memo_detail"),    #int 뒤의 memo_id는 view의 one_memo(memo_id)의 매개변수와 같아야함
    path("", index, name='index'),
    path("search/", search),
    path("memo/create/", memo_create, name='memo_create'),
    path("test1/", test1, name='test1'),
    path("test2/", test2, name='test2'),
    path("memo/update/<int:pk>/", memo_update, name='memo_update'),
    path("memo/delete/<int:pk>/", memo_delete, name='memo_delete'),
    path("memo/mine/", my_memo_list, name = 'my_memo_list'),
    path("memo/search/", memo_search, name='memo_search')
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