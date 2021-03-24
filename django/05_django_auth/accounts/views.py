from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # 저번에 했던 form과 정보 받는 순서가 다르다. (애초에 form이 그렇게 만들어짐 반드시 첫번째로 request가 들어오도록. 두번째는 data객체가 선택적으로 들어옴(사용자의 아이디, 비번). 그래서 data 써도 되고 안써도 됨.) modelform들은 첫번째가 data. 들어오는 인자 보고 이게 뭔지 유추 가능.
        # 사용자가 로그인할 수 있는 Form. 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 저번에는 저장이었는데 이번엔 session이 create된다. 
            # get_user는 return으로 user값이 온다.
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)