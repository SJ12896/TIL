from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 모든 게시글 조회, 변수명은 꼭 복수로. 전체를 조회했으니까
    #articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


# 사용자가 django form에서 데이터를 입력하고 submit해서 데이터가 넘어온 상태 가정
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()

    '''사용자가 /articles/create로 요청을 보낸 경우
    1) GET : 비어있는 ModelForm을 던진다.
    2) POST : 데이터를 받아서 DB에 저장한다.'''

    # if request.method == 'POST':
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         article = form.save()
    #         return redirect('articles:detail', article.pk)
    # else:
    #     form = ArticleForm()
        
    # context = {
    #     'form': form,
    # }
    # return render(request, 'articles/create.html', context)

    if request.method == 'GET':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

    # 1. POST Data가 들어있는 ModelForm 인스턴스 생성
    # form = ArticleForm(request.POST)
    # # 2. Form에 들어있는 데이터에 대한 유효성 검사 실시
    # if form.is_valid(): # boolean 형식으로 들어온다.
    #     # 3. 새로운 Article 인스턴스를 생성하고 DB에 저장한다.
    #     article = form.save()
    #     # 4. 생성한 Article 인스턴스 pk값과 함께 상세정보 페이지로 redirect
    #     return redirect('articles:detail', article.pk)

    # # 유효성 검사에서 탈락했을 때
    # return redirect('articles:new')
        

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


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article' : article,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 수정할 Article 인스턴스 가져오기
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # 수정할 데이터와 수정 대상 인스턴스를 건네준다.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # db에 반영한다. (인스턴스를 받았기 때문에 update
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
        

    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

    # article = Article.objects.get(pk=pk)
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)