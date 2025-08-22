from django.db import models

# Create your models here.
"""
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    investment_style VARCHAR(20) DEFAULT '보수적'
        CHECK (investment_style IN ('보수적', '적극적', '공격적')),
    vip_flag BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
class Article(models.Model) :
    #Article이라는 테이블이 만들어지고 밑에 속성과 내용 작성
    #title이 이름이고
    #CharField가 VARCHAR이고 max_length가 크기 ex)VARCHAR(200)
    title = models.CharField('이게요렇게나옵니다', max_length=200)
    content = models.TextField("content")
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)

    def __str__(self) :
        return "__str__통해서이렇게나옵니다"+self.title
    
    #편의를 위한 단수복수 표현임, 안해도 됨
    class Meta :
        verbose_name = "아티클"
        verbose_name_plural = "아티클들"

#models.py에 Table을 파이썬 코드로 작성합니다
#설계도 작성 : python manage.py makemigrations
#실제 DB에 반영 : python manage.py migrate

#여러분의 DB에 테이블을 생성해 보겠습니다!

#메모장 기능 실습
#models, admin, views, urls 다 추가해야함
class Memo(models.Model) :  #model을 상속받기
    #제목, 내용, 중요여부, 생성일
    title = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    is_important = models.BooleanField('중요', default=False)
    created_at = models.DateField('작성일', auto_now_add=True)

    def __str__(self) :
        return self.title+"작성 완료"

    class Meta :
        verbose_name = "메모"
        verbose_name_plural = "메모 목록"
        ordering = ['created_at']

# ->Admin 페이지 등록
# 3시 부터는 뷰를 같이 만들어 보기