from django.contrib import admin
from .models import Article
from .models import Memo
# Register your models here.

#이렇게 하면 간단, 하지만 보기에 맘에 안들면 아래 커스텀 방법
#admin.site.register(Article)

#이렇게 하면 커스텀 가능
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin) :
    list_display = ['title', 'created_at', 'updated_at']    #목록에 표시할 필드
    search_fields = ['title', 'content'] #검색 가능한 필드
    list_filter = ['created_at']    #필터 옵션

#제미나이에 polls앱에 아티클 모델을 어드민 페이지에 등록 해줘. 제목과 콘텐츠 10그라만 표현되게 해줘 라고 해보기

#admin.py에서 우리가 만든 모델 등록하는 것을 해보겠습니다
#샘플도 확인하시고 다른 둘(제미나이, gpt)를 이용해서 구조를 만들어서 적용도 해보겠습니다

#만약 모델 만드는 과정에서 문제가 생기면
#sqlite 파일 삭제해서 진행하시면 됩니다
#하지만 이게 자주 반복되면 곤란합니다

#Memo import 하기
@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin) :
    list_display = ['title', 'is_important', 'created_at']
    list_filter = ['is_important', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_important']