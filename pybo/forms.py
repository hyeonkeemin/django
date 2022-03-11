from django import forms # 페이지 요청시 전달되는 파라미터들을 쉽게 관리하기 위해 사용하는 클래스. 필수 파라미터가 누락되지않았는지, 파라미터 형태가 적절한지 검증.
                        # HTML 자동생성하거나 폼에 연결된 모델을 이용하여 데이터 저장도 가능함.
from pybo.models import Question, Answer

# 장고의 폼은 일반 폼(forms.Form)과 모델 폼(forms.ModelForm)이 있음. 모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할 수 있는 폼
# 모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요함. Meta 클래스에는 사용할 모델과 모델의 속성을 정의해야함

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성

        # widgets = { # Meta 클래스의 widgets 속성을 지정하면 입력 필드에 form-contorl과 같은 부트스트랩 클래스를 추가할 수 있음.
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        # 질문등록 화면에서 영어를 한글로 변경
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용'
        }