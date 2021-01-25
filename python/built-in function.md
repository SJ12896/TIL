### 1. all()

> *iterable* 의 모든 요소가 참이면 (또는 iterable 이 비어있으면) `True` 를 돌려줍니다.1.

```python
>>> print(all([1,2,3,'a']))
True
>>> print(all([]))
True
>>> print(all([9,5,7,0,'']))
False
>>> 
```



### 2. any()

> *iterable* 의 요소 중 어느 하나라도 참이면 `True` 를 돌려줍니다. iterable이 비어 있으면 `False` 를 돌려줍니다. 

```python
>>> print(any([1,0]))
True
>>> print(any([]))
False
>>> print(any([0]))
False
>>> 
```



[출처 : python docs](https://docs.python.org/ko/3.8/)