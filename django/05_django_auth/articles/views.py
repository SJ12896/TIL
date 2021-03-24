from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# create를 누르면 자동으로 index로 보내진다. 대신 url이 http://127.0.0.1:8000/accounts/login/?next=/articles/create/ 로 달라져있다. decorator로 이동한 경우 원래 가려고 했던 곳을 next로 붙여주고, 로그인 시 바로 연결된다. 근데 우리가 직접 처리해야한다. url 달라진 상태에서 그냥 로그인하면 평소처럼 index로 간다. 작업은 accounts의 login 함수에서 처리한다.
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

# @login_required를 delete에서는 함께 사용할 수 없었다. 405 error가 생긴다.
@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        article.delete()
    return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
        

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        # 댓글 작성을 위한 form은 이미 detail에 있다. get, post를 나눌 필요 없고 
        # 새 댓글을 위한 get말고 post만 처리하면 된다.
        # 인자로 받은 pk를 사용해도 되지만 정확히 명시하기 위해 article따로 만들기
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'comment_form' : comment_form,
            'article' : article,
        }
        return render(request, 'articles/detail.html', context)
    return HttpResponse(status=401)
    # return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)