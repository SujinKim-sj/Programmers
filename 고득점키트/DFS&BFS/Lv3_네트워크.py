from collections import deque
def bfs(n, computers, cur, visited):
    visited[cur] = True
    q = deque()
    q.append(cur)

    while q:
        cur = q.popleft()
        visited[cur] = True
        for i in range(n):
            if i != cur and computers[cur][i] == 1:
                if not visited[i]:
                    q.append(i)

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i, visited)
            answer += 1

    return answer