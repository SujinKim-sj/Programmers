def solution(a, b):
    answer = 0

    if a == b:
        answer = a
    elif a < b:
        for i in range(a, b + 1):
            answer += i
    else:
        for i in range(b, a + 1):
            answer += i

    return answer


# 다른 사람의 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

def adder2(a, b):
    return (abs(a-b)+1)*(a+b)//2        # 절댓값 사용
