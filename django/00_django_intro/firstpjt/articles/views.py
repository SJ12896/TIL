import random
import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')


def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name' : 'HARRY'
    }
    context = {
        'info' : info,
        'foods': foods,}
    return render(request, 'articles/greeting.html', context)


def dinner(request):
    foods = ['족발', '피자', '햄버거', '초밥', '굶기']
    pick = random.choice(foods)
    today = datetime.datetime.now()
    context = {
        'pick': pick,
        'foods': foods,
        'today': today,
    }
    return render(request, 'articles/dinner.html', context)


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'articles/catch.html', context)


def hello(request, name):
    context={
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)


def dtl_practice(request):
    fruits = [
        'mango',
        'blueberry',
        'coconut',
        'kiwi',
        'melon',
    ]
    foods = [
        'pizza',
        'sushi',
        'pork belly',
        'spaghetti',
    ]
    user_list = []
    context = {
        'fruits' : fruits,
        'foods' : foods,
        'user_list' : user_list,
    }
    return render(request, 'articles/dtl_practice.html', context)