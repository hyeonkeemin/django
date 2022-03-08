from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    '''
    pybo 목록 출력
    '''
    question_list = Question.objects.order_by('-create_date') # order_by: 조회한 데이터를 특정 속성으로 정렬, '-create_date'는 -기호가 앞에 붙어있어 작성일시의 역순을 의미
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context) # context에 있는 Question 모델 데이터 question_list를 'pybo/question_list.html' 파일에 적용하여 html 코드로 반환

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    # question = Question.objects.get(id=question_id) # URL 매핑에 있던 question_id: /pybo/2/ 페이지가 호출되면 최종으로 detail 함수의 매개변수 question_id에 2가 전달
    question = get_object_or_404(Question, pk=question_id) # 존재하지 않는 페이지에 접속하면 오류 대신 404 페이지 출력
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)