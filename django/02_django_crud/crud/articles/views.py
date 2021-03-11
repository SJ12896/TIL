from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # 모든 게시글 조회, 변수명은 꼭 복수로. 전체를 조회했으니까
    #articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # get 요청으로 돌어온 사용자 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    # article 모델 클래스 기반으로 인스턴스를 만든다.
    # 사용자 데이터를 넘겨주고 초기화한다.
    article = Article(title=title, content=content)
    # db에 저장한다.
    article.save()
    # return redirect('/articles/') 이렇게 하지 말기
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)