# DFS/BFS - Lv2. 게임 맵 최단거리

from collections import deque


def solution(maps):
    answer = 0
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((0, 0))

    maps[0][0] = 1

    while (q):
        x, y = q.popleft()

        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < len(maps) and 0 <= dy < len(maps[0]):
                if maps[dx][dy] == 1:
                    maps[dx][dy] = maps[x][y] + 1
                    q.append((dx, dy))

    # maps[n - 1][m - 1]의 값
    answer = maps[len(maps) - 1][len(maps[0]) - 1]

    if answer == 1:  # 상대 팀 진영에 도달할 방법이 없을 경우
        return -1
    else:
        return answer