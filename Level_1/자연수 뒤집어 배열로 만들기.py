# 나의 풀이
def solution(n):
    answer = []
    n2 =  str(n)

    for i in range(len(n2), 0, -1):
        answer.append(int(n2[i - 1]))

    return answer


# 다른 사람의 풀이
def digit_reverse(n):
    return list(map(int, reversed(str(n))))