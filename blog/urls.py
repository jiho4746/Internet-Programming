from django.urls import path
from . import views

urlpatterns = [ #서버IP/blog/
    # myInternetPrj의 urls - blog의 urls - view - html 연결

    # <FBV 스타일로 페이지 만들기 - 직접 html에 연결>
    # 서버IP/blog
    #path('', views.index),
    # 서버IP/blog 상세 페이지
    #path('<int:pk>/', views.single_post_page),

    # <CBV 스타일로 페이지 만들기>
    # 블로그 목록
    path('', views.PostList.as_view()),
    # 블로그 상세 페이지
    path('<int:pk>/', views.PostDetail.as_view()),
]