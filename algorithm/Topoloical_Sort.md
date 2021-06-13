## Topological Sort 위상정렬

- [위상정렬](https://ko.wikipedia.org/wiki/%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC) : 유향 그래프의 꼭짓점들을 변의 방향을 거스르지 않도록 나열하는 것. 대표적인 예시는 대학의 선수과목. 그래프에 반드시 순환이 존재하지 않아야 한다. `비순환 유향 그래프`여야 한다.

- `이것이 취업을 위한 코딩테스트다 with 파이썬 - 나동빈 지음, 한빛미디어 출판`을 보고 정리한 내용 (p.290)
  - 진입차수을 알아야한다. 특정 노드로 들어오는 간선의 개수 의미
  - 진입차수 0인 노드 큐에 넣기 -> 큐가 빌 때 까지 (1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거 / 2. 새롭게 진입차수가 0이 된 노드를 큐에 넣기)
  - 모든 원소 방문 전에 큐가 빈다면 사이클이 존재 -> 위상 정렬 불가능

- 14567문제에서 적용

```python
def topology_sort():
    q = deque([])
    # 위상정렬을 시작할 때 진입차수가 0인 노드들을 먼저 q에 넣는다.
    # 이 문제에선 각 과목을 듣기 위해 몇 학기를 들어야하는지 계산
    for i in range(len(indegree)):
        if not indegree[i]:
            q.append([i, 1])
        result[i] = 1

    while q:
        x, time = q.popleft()
        # 현재 과목을 선수과목으로 하는 과목들 -> i
        # 현재 과목은 수강했으므로 그 과목들에서 진입차수를 -1
        for i in subjects[x]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append([i, time+1])
                result[i] = time+1

                
for m in range(M):
    a, b = map(int, input().split())
    subjects[a-1].append(b-1)
    # 각 노드마다 진입차수 계산
    indegree[b-1] += 1
```

