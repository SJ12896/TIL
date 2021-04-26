from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id' : article.pk,
                'content' : article.content,
            }
        )
    # dictionary가 아닌 다른 타입이 json으로 바뀌면 safe옵션 False로 
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    # 이미 json이라 jsonresponse말고 httpresponse, http 통신간의 content type 지정 필요
    return HttpResponse(data, content_type='application/json')


@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    # 단일 객체냐 아니냐 many로 표현. 기본 값이 False
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)