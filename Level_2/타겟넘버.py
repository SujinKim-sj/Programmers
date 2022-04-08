from collections import deque


# BFS 로 구현
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    while queue:
        tmp, idx = queue.popleft()
        idx += 1

        if idx < n:
            queue.append([tmp + numbers[idx], idx])
            queue.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    return answer


# DFS 로 구현
def solution2(numbers, target):
    n = len(numbers)
    answer = 0

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    dfs(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution2([4, 1, 2, 1], 4))