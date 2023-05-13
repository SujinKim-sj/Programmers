# 완전탐색 LV2 - 피로도

from itertools import permutations


# 1) 순열로 풀기
def solution(k, dungeons):
    answer = 0

    for p in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0

        for need, spend in p:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        answer = max(answer, cnt)
    return answer


# 2) 백트래킹으로 풀기
# answer = 0

def dfs(k, count, dungeons, visited):
    global answer
    if count > answer:
        answer = count

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], count + 1, dungeons, visited)
            visited[i] = False


def solution2(k, dungeons):
    global answer
    visited = [False] * len(dungeons)

    dfs(k, 0, dungeons, visited)

    return answer