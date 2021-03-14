### 재귀함수 호출 공부

[출처](https://youtu.be/apuLBFfGlQs)



> 테이블에 2명 이상 앉는 방법 구하기. 테이블에는 최대 10명까지 앉을 수 있다. 순서는 신경쓰지 않는다.





- 공통 코드. 변하지 않는 수를 변수로 지정한다.

```python
n = int(input())
min_ = 2 # 테이블에 앉을 수 있는 최소 사람 수
max_ = 10 # 테이블에 앉을 수 있는 최대 사람 수
```



1) global을 사용해 가능한 경우 셀 때

```python
cnt = 0
# 매개변수에 현재 남아있는 앉을 사람 수, 이번에 앉힐 사람 수를 넣는다.
def sit(seat, not_yet):
    global cnt
    # 테이블에 10명까지 앉을 수 있지만 남아있는 사람보다 적은 수가 앉을 수 없으니까 0보다 작은 경우엔 return
    if seat < 0:
        return
   	# 남아있는 앉을 사람이 딱 0이라면 성공 +1을 한다.
    elif seat == 0:
        cnt += 1
        return
    # 이 문제에서는 순서가 상관없기 때문에 2, 4 로 앉을 때와 4, 2로 앉을 때는 같은 경우라고 생각한다. 따라서 다음에 앉힐 사람 수가 현재 앉힐 사람 수보다 같거나 큰 경우만 계산해서 4, 2 순서로 앉는 경우는 고려하지 않는다.
    for i in range(not_yet, max_+1):
        sit(seat-i, i)


sit(n, min_)
print(cnt)
```



2) return에서 최종 값을 받아올 때

```python
def sit(seat, not_yet):
    if seat < 0:
        return 0
    elif seat == 0:
        return 1

    # 여기서 cnt = 0을 지정해서 누적되지 않고 각 경우마다 가능(1), 불가능(0)값을 받아온다. 더해지는 cnt는 맨 위에 호출했을 당시의 cnt에 누적된다.
    cnt = 0
    for i in range(not_yet, max_+1):
        cnt += sit(seat-i, i)
    return cnt


print(sit(n, min_))
```





3) 메모이제이션 : 시간이 엄청 단축된다.

```python
memo = {}
def sit(seat, not_yet):
    # (남아있는 앉을 사람, 이번에 앉힐 사람)을 하나의 key로 만들어서 딕셔너리에 저장하고 같은 상황에서는 그 값을 재활용한다. 
    key = str((seat, not_yet))
    if key in memo:
        return memo[key]
    if seat < 0:
        return 0
    elif seat == 0:
        return 1

    cnt = 0
    for i in range(not_yet, max_+1):
        cnt += sit(seat-i, i)
    # 메모 저장 부분
    memo[key] = cnt
    return cnt
```

