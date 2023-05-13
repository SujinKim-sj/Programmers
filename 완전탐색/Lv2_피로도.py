# 완전탐색 LV2 - 피로도

answer = 0

def dfs(k, count, dungeons, visited):
    global answer
    if count > answer:
        answer = count

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons, visited)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)

    dfs(k, 0, dungeons, visited)

    return answer