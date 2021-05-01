## Class based View

<br>

articles/urls.py

```python
from django.urls import path
from django.views.generic import TemplateView
from . views import AboutView, IndexView, ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from . import views

app_name = 'articles'
urlpatterns = [
    # urls.py에서 보낼 TemplateView를 사용하고 template이름을 바로 알려줘서 view에 들리지 않고 바로 페이지를 보여준다.
    path('about/', TemplateView.as_view(template_name="articles/about.html")),
    
    # about에서 사용한 것 과 같은 TemplateView를 이용하는데 views.py에서 TemplateView를 상속받은 나의 class view를 만들어서 사용했다. 주로 이 방법 사용
    path('about3/', AboutView.as_view()),
        
    # django.views의 View를 상속받아 만든 class view이용, request method에 따라 분기. 자세한 내용은 views.py에서
    path('index2/', IndexView.as_view()),
    
    # 이 밑으로는 django.views.generic에 존재하는 view를 사용했다. 자세한 내용은 views.py에서
    path('', ArticleListView.as_view(), name='index'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('create/', ArticleCreateView.as_view(), name='create'), 
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete'),
]
```

<br>

- django generic view : 같은 패턴의 반복을 줄여주기 위해 만들어졌다. 많이 사용되는 패턴을 가져와 추상화했다. modelform, modelserializer와 비슷한 방식으로 사용할 수 있다. 사용할 모델 명을 알려주고 그 외 자잘한 설정을 나에게 편한 방식으로 변경해주면 된다.

- articles/views.py

```python
from django.shortcuts import render, get_list_or_404
from django.views.generic import TemplateView
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Article



class AboutView(TemplateView):
    template_name = 'articles/about3.html'


# 평소에 사용하던 함수 기반 뷰에서 if문으로 request.method를 분기하던 것과 다르게 django.views의 View를 상속받아 만든 class based view에서는 클래스 안의 함수를 통해 분기할 수 있다.
class IndexView(View):
    def get(self, request):
        articles = get_list_or_404(Article)
        context = {
            'articles' : articles,
        }
        return render(request, 'articles/index2.html', context)

# 자동으로 연결되는 template name은 appname_list.html이다.
# model에 존재하는 데이터를 보여준다.
class ArticleListView(ListView):
    model = Article
    # html 페이지에서 사용될 context명 지정. 지정하지 않을 시 object_list가 기본 이름이다.
    context_object_name = 'articles'
    queryset = Article.objects.order_by('-id')
    # template_name = 'articles/index2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context에 담아서 넘길 데이터 추가
        context['name'] = 'change'
        return context

# 자동으로 연결되는 template name은 appname_detail.html이다. 
# context name을 변경하지 않았으므로 object, object.title 등을 통해 화면에 출력
class ArticleDetailView(DetailView):
    model = Article

# 자동으로 연결되는 template name은 appname_form.html이다.
# LoginRequiredMixin을 사용해 데코레이터, 함수를 사용하지 않고 로그인한 사용자만 글을 쓸 수 있게 만들다. 로그인은 자동으로 accounts 앱의 templates/registration/login.html에 연결되는데 템플릿 안의 폴더명이 앱 명과 똑같지 않으니 주의해야 한다.
# 또한 project의 url 에서도 path('accounts/', include('django.contrib.auth.urls')), 처럼 만든다. 
# 그 전에 settings.py에 LOGIN_REDIRECT_URL = 'articles:index' 을 설정해서 로그인 성공 후 향할 url을 정해둔다.
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# update역시 자동으로 연결되는 template name은 create할 때 와 같은appname_form.html이다. 다른 설정을 내가 해주지 않아도 전에 입력되있던 데이터가 알아서 들어가있다.
class ArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'

# delete는 성공하고 나면 자동으로 갈 곳이 없기 때문에 따로 지정해줘야 한다. 또한 그 전에 삭제하면 appname_confirm_delete.html로 연결돼서 삭제 확인을 받는다. 삭제 확인할 때도 다른 거 필요없이 그냥 POST방식으로 작동하는 submit만 만들어주면 된다. 아주 편리
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:index')
```

<br>

- articles/models.py

```python
from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # get_abosulte_url을 통해서 글 번호마다 다른 url이 생성되는 걸 하드 코딩해줄 필요없이 해당 번호에 맞는 detail 페이지로 이동하 ㄹ수 있다. <a href = "{{ object.get_abolsute_url }}"> {{ object.name}}
    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"pk": self.pk})
    
```

