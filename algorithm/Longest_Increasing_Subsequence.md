### Longest Increasing Subsequence 최장 증가 부분 수열(LIS)

- [최장 증가 부분 수열](https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EC%A6%9D%EA%B0%80_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4) : 주어진 수열에서 오름차순으로 정렬된 가장 긴 부분수열을 찾는다. 연속적이거나 유일할 필요 없다.

<br>

#### 1. dp

- 11055번 풀이 참고
- 배열 2번째부터 끝까지 수를 순회하면서 현재 숫자보다 작은 앞 부분 숫자가 존재할 때 앞 부분 숫자의 result배열 길이가 현재 숫자 result보다 길면 업데이트 한다.

```python
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if data[j] < data[i]:
            result[i] = max(result[j]+data[i], result[i])
```

<br>

#### 2. 이진탐색

- 12015번 풀이 참고
- dp에서 시간초과가 날 수 있다. 
- result에 배열 첫 숫자 넣고 두 번째 숫자부터 끝까지 순회한다. 현재 숫자가 result의 마지막 값보다 크다면 바로 append하고 아니라면 이진탐색을 사용한 find_loc를 통해 들어갈 위치를 정해준다.
- 여기선 result 배열이 진짜 증가 부분 수열 자체가 아니라 길이를 찾을 때 사용한다.

```python
def find_loc(x):
    l, r = 0, len(result)-1
    idx = -1
    while l <= r:
        m = (l+r) // 2
        if result[m] > x:
            idx = m
            r = m - 1
        elif result[m] == x:
            return
        else:
            l = m + 1
    result[idx] = x


for i in range(1, N):
    if result[-1] < nums[i]:
        result.append(nums[i])
    else:
        find_loc(nums[i])
```



