### Next Permutation Algorithm
- 다음 순열 찾기 / 전체 순열 탐색 알고리즘
- 솔직히 왜 저런식으로 되는건지 완전히 이해 되는 건 아니라서 일단 외운다...

```python
data = [8, 2, 34, 9, 7, 12, 78]

idx = 0
# 전체 리스트를 순회하면서 data[i] < data[i+1]인 마지막
# idx를 찾는다. 순서대로 나열된 숫자에서 data[i+1]이 data[i]보다 크면 다음 순열이 시작될 가능성을 가진다. 따라서 data 안에서 여러 개가 등장해도 가장 마지막을 기준으로 잡는다.
for i in range(len(data)-1):
    if data[i] < data[i+1]:
        idx = i

change = 0
# 앞에서 구한 교환 위치 다음부터 리스트 끝까지 중 교환 위치의
# 값보다 크다면 바꿀 위치로 정한다.
for i in range(idx+1, len(data)):
    if data[i] > data[idx]:
        change = i

# 두 숫자 교환
data[idx], data[change] = data[change], data[idx]

# 교환된 곳 뒤부터 정렬
data[idx+1:] = sorted(data[idx+1:])

print(data)

```

