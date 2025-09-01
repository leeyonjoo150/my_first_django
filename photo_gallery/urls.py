from django.urls import path
from .views import photo_list, photo_create, photo_detail, photo_update, photo_delete, photo_like, my_photos, photo_like_ajax
#원하는 뷰를 가져오는 형태
#이렇게도 가능
#from polls import index, hello, lion, good, debug_request

app_name = 'photo_gallery'


urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('create/', photo_create, name='photo_create'),
    path('<int:pk>/', photo_detail, name='photo_detail'),
    path('<int:pk>/edit/', photo_update, name='photo_update'),
    path('<int:pk>/delete/', photo_delete, name='photo_delete'),
    path('<int:pk>/like/', photo_like, name='photo_like'),
    path('my/', my_photos, name='my_photos'),
    path('<int:pk>/like_ajax/', photo_like_ajax, name="photo_like_ajax")
]
