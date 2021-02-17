### Bayby-gin Game

> 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑았을 때
> 3장의 카드가 연속적인 번호를 갖는 경우를 run이라 하고
> 3장의 카드가 동일한 번호를 갖는 경우를 triplet이라고 한다.
>
> 그리고, 6장의 카드가 run과 triplet으로만 구성된 경우를 baby-gin으로 부른다.
>
> 6자리의 숫자를 입력 받아 baby-gin 여부를 판단하는 프로그램을 작성하라.
> (baby-gin 일 경우 **1,** 아닌 경우 **0** 을 출력한다.)



```python
T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input()))
    cntN = [0] * 10

    # 카운팅 정렬을 사용했다.
    for number in numbers:
        cntN[number] += 1

    # 먼저 triplet이 성립하는 경우를 찾았다. 여기서 틀렸던 이유는 triplet만 2번 나올 수 있는 경우를 고려하지 않았다. 
    result = 0
    for i in range(len(cntN)-1):
        if cntN[i] / 3 > 0:
            result += (cntN[i] // 3)
            cntN[i] -= (cntN[i] // 3) * 3

    # run이 성립하는 경우를 찾았다. 여기서 틀렸던 이유는 run이 2번 나올 때 그 중 겹치는 숫자가 있을 경우를 고려하지 않았다. 그래서 for문을 사용했다가 while문으로 변경했다.
    i = 1
    while True:
        if (result == 2) or (i == len(cntN)-1):
            break

        if cntN[i-1] and cntN[i] and cntN[i+1]:
            cntN[i-1] -= 1
            cntN[i] -= 1
            cntN[i+1] -= 1
            result += 1
            continue

        i += 1

    if result == 2:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))


```

