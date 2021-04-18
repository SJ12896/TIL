## Django allauth

- 공식 문서 따라하다가 요약 & 이해안되는 부분 공부

### 0. 사전작업

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) 에서 Installation 절차를 따라한다.
- django-allauth의 Providers에서 내가 사용할 사이트 별로 나와있는 App registration절차를 거친다.

### 1. Kakao

- [공식 문서](https://developers.kakao.com/docs)

- 카카오 로그인 : 카카오 계정과 앱 연결 / 토큰 발급받아 카카오 API 사용
  - 액세스 토큰Access Token : 사용자 인증, 카카오 API 호출 권한 부여
  - 리프레스 토큰Refresh Token : 액세스 토큰 갱신
- 로그아웃 : 로그인 통해 발급받은 토큰 만료시켜 사용자가 로그아웃 요청했을 때나 서버에서 특정 사용자 로그아웃 요청할 때 로그아웃
- 연결 끊기 : 카카오 계정과 앱의 연결 끊기. 앱에서 더 이상 해당 사용자 API호출 불가, 카카오 플랫폼에서도 해당 앱에 대한 해당 사용자 데이터 지워짐

#### 1-1. 로그인 (REST API)

- Kakao SDK for Android, iOS, Javascript와 REST API로 제공되며 OAuth 2.0기반
- 별 생각없이 웹페이지면 REST API를 사용해야할 거 같아서 REST API로 열심히 구현했는데 정리하려고 보니까 Javascript SDK를 사용했으면 훨씬 편했을 거라는 생각이 든다. 무턱대고 시작하지 말고 좀 더 알아보고 시작할 것을...
- JavaScript SDK는 스마트폰에서 카카오톡에 연결된 카카오 계정 정보를 바로 이용하고 REST API는 카카오 계정 정보 입력 웹페이지를 사용하는데 여기서 카카오톡으로 로그인을 클릭하면 연결된 카카오 계정 정보를 이용할 수 있다. -> REST API는 계정은 있는데 카카오톡 어플을 삭제한 사람도 이용할 수 있어서 좋은건가?

---

- [소프트웨어 개발 키트 SDK](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EA%B0%9C%EB%B0%9C_%ED%82%A4%ED%8A%B8#cite_note-ShamseeCCNA15-1) : Software Development Kit. 특정 소프트웨어 꾸러미, 프레임워크, 하드웨어 플랫폼, 컴퓨터 시스템 등을 위한 응용 프로그램을 만들 수 있게 해주는 개발 도구의 집합. 응용 프로그램을 만들기 위해서 특정 SDK를 다운로드 받아야 한다.
- [애플리케이션 프로그래밍 인터페이스 API](https://ko.wikipedia.org/wiki/API) : Application Programming Interface. 응용 프로그램에서 사용할 수 있도록 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스.

---

- 단계 : 카카오톡으로 간편 로그인 -> 카카오 계정 자격정보(Credentials)를 통해 사용자 인식, 올바르면 정보 및 기능 활용 동의받기 -> 동의한 뒤 `인가 코드(Authrozation Code) `발급. Redirect URI에 전달 -> 앱에서 전달 받은 인가 코드 기반으로 `토큰(액세스, 리프레시)` 요청하고 받기
- 액세스 토큰 : 사용자 인증. 카카오 API 호출 권한 부여
- 리프레시 토큰 : 매번 카카오 계정 정보를 입력하거나 카카오톡으로 로그인하지 않고도 액세스 토큰 발급

<br/>

##### 인가 코드 받기

accounts/views.py

- 발급받은 REST_API_KEY와 사이트에 등록한 REDIRECT_URI를 통해 인가 코드를 요청한다. 사용자가 동의했을 시 REDIRECT_URI에 인가 코드가 붙어 온다.

```python
@require_safe
def kakao_login(request):
    REST_API_KEY = '...'
    REDIRECT_URI = 'http://localhost:8000/accounts/kakao/login/callback/'
    return redirect(f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code')
```

<br/>

##### 토큰 받기

- 받은 인가 코드로 액세스 토큰과 리프레시 토큰을 발급받아야 한다. 필수 파라미터 값을 담아 POST로 요청. 응답은 JSON 객체로 Redirect URI에 전달된다.

accounts/views.py

- 토큰 발급받는 요청을 위해 requests 라이브러리를 import했다. requests는 http요청을 간단하고 인간친화적이게 할 수 있도록 도와준다.

```python
import requests
import json

def kakao_callback(request):
    REST_API_KEY = '...'
    REDIRECT_URI = 'http://localhost:8000/accounts/kakao/login/callback/'
    code = request.GET.get('code')
        
    token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}")

    token_request_json = token_request.json()

    ACCESS_TOKEN = token_request_json['access_token']
```

<br/>

##### 사용자 정보 가져오기

- 사전에 kakao develpoers 사이트에서 동의 항목 설정 필수
- 액세스 토큰 사용 or 앱 어드민 키 사용 두 가지 방법으로 제공
- 사용자 액세스 토큰 or 어드민 키를 헤더에 담아 GET 또는 POST로 요청. 성공시 응답 바디는 JSON 객체로 사용자 정보 포함.

accounts/views.py

- 액세스 토큰 사용
- 이 후 받아온 사용자 값의 id가 나의 User db에 존재한다면 바로 로그인, 아니라면 User db에 등록하는 절차를 거친다. 이 부분에서 password가 아예 존재하지 않는데 어떻게 해야할지 고민했는데 django의 User 메서드에 `set_unusable_password`가 존재했다. 신기했다. 이 메서드를 사용하면 check_password는 False값만 나온다고 한다.
- 이후 login 부부에서 또 에러가 계속 생겼는데 multiple authentication backends configured and therefore must provide the `backend` argument or set the `backend` attribute on the user 
- django-allauth Installation 부분에서 settings.py에 AUTHENTICATION_BACKENDS 값을 2개로 설정했기 때문에 생긴일이다. 일반 로그인 backend를 사용할 거라서 명시해준다.

```python
def kakao_callback(request):
    ...
    ACCESS_TOKEN = token_request_json['access_token']
    
    profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
        )

    profile_request_json = profile_request.json()
    
    if not User.objects.filter(username=profile_request_json['id']).exists():
        user = User(
            username=profile_request_json['id'], 
            first_name=profile_request_json['properties']['nickname'], 
            )
        user.set_unusable_password()
        user.save()
    else:
        user = User.objects.get(username=profile_request_json['id'])
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')

    return redirect('pages:index')
```

