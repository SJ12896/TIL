### REST framework : HTML & Forms

- [HTML & Forms](https://www.django-rest-framework.org/topics/html-and-forms)
- 앞서 수업시간에 배웠을 때는 POSTMAN으로 정보를 보내고 받는 과정만 다뤘기 때문에 웹페이지에서 REST framework를 적용해서 화면상에 출력하는 과정에 대해 공부해봤다.
- REST framework는 API 스타일 응답, HTML페이지 return에 모두 적합하며 serializer는 HTML form으로 사용될 수 있으며 templates render가능
- HTML response를 위해 `TemplateHTMLRenderer` 또는 `StaticHTMLRenderer`를 사용할 수 있다. 첫번째는 dictionary 형태의 context data를 포함한 응답하며 view나 응답 과정에서 구체화된 template 기반의 html page를 render한다. 
- serializer는 `render_form` 템플렛 태그를 사용해 form으로 렌더링 할 수 있다. 그리고 serializer instance는 template의 context로 포함될 수 있다. 

---

- 그런데 의문점 : rest api를 사용할 때 수정은 put method로 배웠는데 html form은 get, post method만 지원한다고 한다. 어떻게 우회해서 put을 사용할 수 있다고는 하는데 이렇게 쓰는게 rest api 인가? rest api가 뭔지 어렵다.

<br>

- 실습 : 회원정보 수정

accounts/serializers.py

- serializer에서도 회원정보 중 보여주고 싶은 부분만 나오도록 fields를 수정했다.

```python
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'date_of_birth', 'cell_phone', )
```



accounts/views.py

```python
class UserView(APIView):
    template_name = 'accounts/user_detail.html'
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, username):
        person = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(person)
        return Response({'serializer' : serializer, 'person' : person})
    
    def post(self, request, username):
        person = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(person, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return redirect('accounts:user-info', person.username)
        return Response({'serializer' : serializer, 'person' : person})
```

<br>

accounts/user-detail.html

```html
{% extends 'base.html' %}
{% load rest_framework %}

{% block content %}
<h1>{{ person.username }}의 페이지입니다.</h1>
<form action="" method="POST">
{% csrf_token %}
{% render_form serializer %}
<input type="submit" value="저장">
</form>
{% endblock content %}
```



