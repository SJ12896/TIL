from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request, context):
    # 모든 게시글 조회, 변수명은 꼭 복수로. 전체를 조회했으니까
    #articles = Article.objects.all()[::-1]
    # articles = Article.objects.order_by('-pk')
    context = {
        'articles' : context,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # get 요청으로 돌어온 사용자 데이터 추출
    title = request.GET.get('title')
    content = request.GET.get('content')

    # article 모델 클래스 기반으로 인스턴스를 만든다.
    # 사용자 데이터를 넘겨주고 초기화한다.
    article = Article(title=title, content=content)
    # db에 저장한다.
    article.save()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)
