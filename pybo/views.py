from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

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


def answer_create(request, question_id): # request: question.html에서 textarea에 입력된 파이썬 객체 // question_id: URL 매핑 정보값
    ''''
    pybo 답변 등록
    '''
    question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), # textarea에 입력된 파이썬 객체에 담겨진 값을 추출하기 위한 코드.
    #                                                                 # Question 모델을 통해 Answer 모델 생성을 위해 answer_set.create 활용
    #                            create_date = timezone.now())
    # # request.POST.get('content')는 POST 형식으로 전송된 form 데이터 항목 중 name이 content인 값을 의미
    # # Answer 모델이 Question 모델을 FK로 참조하고 있으므로 question.answer_set같은 표현 사용가능
    #
    # return redirect('pybo:detail', question_id=question.id) # redirect: 함수에 전달된 값을 참고하여 페이지 이동 수행

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else: # 답변 등록은 POST 방식만 사용되기 때문에 else 구문에서 호출되지 않으나, 패턴의 통일성을 위해 작성
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    '''
    pybo 질문 등록
    '''

    if request.method == 'POST': # 질문 등록 후 저장하기 버튼을 클릭하면 POST 방식으로 요청됨. form 태그에 action 속성이 지정되지 않으면 페이지가 디폴트 action으로 설정됨
                                # 저장하기를 누르면 question_create 함수가 실행되고 request.method 값은 POST가 되어 다음 코드들이 실행됨.
        form = QuestionForm(request.POST)
        if form.is_valid(): # form이 유효한지 검사함.
            question = form.save(commit=False) # form으로 Question 데이터를 저장하기 위한 코드. QuestionForm이 Question 모델과 연결된 폼이기 때문에 이와같이 사용.
                                                # commit=False는 임시저장을 의미. 즉, 실제 데이터에는 아직 데이터베이스에 저장되지 않은 상태.
                                                # 위 옵션을 주지 않으면 create_date에 값이 없다는 오류가 발생함. QuestionForm에는 현재 subject, content 속성만 정의됐고
                                                # create_date 속성은 없기 때문. 이 때문에 임시 저장한 후 question 객체를 리턴 받아 create_date에 값을 설정한 후 question.save()
            question.create_date = timezone.now() # 데이터 저장 시점에 자동 생성해야 하는 값이므로 QuestionForm에 등록하지 않음
            question.save()
            return redirect('pybo:index') # 질문화면 목록으로 이동

    else: # "질문 등록하기" 버튼을 클릭한 경우에는 페이지가 GET 방식으로 요청되어 위 함수가 실행됨. 링크를 통해 페이지를 요청할 때는 무조건 GET 방식이 사용됨

        form = QuestionForm()
    context = {'form': form} # {'form': form}은 템플릿에서 질문 등록시 사용할 폼 엘리먼트를 생성할 때 쓰임

    return render(request, 'pybo/question_form.html', context)
