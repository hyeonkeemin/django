from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # Question 모델 데이터 중 id 값이 2 인 데이터를 조회하라
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'), # form 엘리먼트의 URL 매핑 추가
    path('question/create/', views.question_create, name='question_create'),
]