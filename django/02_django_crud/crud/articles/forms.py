from django import forms
from .models import Article

# # django form class

# # Article 관련 데이터를 처리할 수 있는 django form
# class ArticleForm(forms.Form):
#     # REGION_A = 'seoul'
#     # REGION_B = 'gwangju'
#     # REGION_C = 'gumi'
#     # REGION_D = 'daegeon'
#     # REGIONS_CHOICES = [
#     #     (REGION_A, '서울'),
#     #     (REGION_B, '광주'),
#     #     (REGION_C, '구미'),
#     #     (REGION_D, '대전'),
#     # ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea) # 여긴 textfield가 없다
#     # region = forms.ChoiceField(choices=REGIONS_CHOICES, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):
    # # 이미 있는 필드를 재정의해서 커스터마이징하기
    # title = forms.CharField(
    #     # label='제목',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class' : 'my-title',
    #             'placeholder' : '제목을 입력해주세요.',
    #         }
    #     ),
    #     # error_messages={
    #     #     'required': '장난치지 말랬지 입력해라...'
    #     # }
    # )

    # content = forms.CharField(
    #     # label='내용',
    #     widget=forms.Textarea(
    #         attrs={
    #             'rows': 5,
    #             'cols' : 20,
    #             'placeholder' : '내용을 입력해주세요.',
    #             'class' : 'my-content',
    #         }
    #     )
    # )
    
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
        'title' : '제목',
        'content' : '내용',
        }
        error_messages = {
            'title': {
                'required' : '장난 ㄴ'
            }
        }
        # exclude= ('title',)