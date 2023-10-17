from collections import Counter
def solution(clothes):
    answer = 0
    cnt = 1
    c = dict(clothes)
    c2 = Counter(c.values())

    for i in c2:
        cnt *= (c2[i] + 1)

    answer = cnt - 1
    return answer

def solution2(clothes): # Counter 사용안하고 풀기
    answer = 1
    c = {}

    for i, j in clothes:
        if j not in c:
            c[j] = 2
        else:
            c[j] += 1

    for i in c.values():
        answer *= i

    answer -= 1
    return answer