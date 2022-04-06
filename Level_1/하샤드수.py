# 나의 풀이
def solution(x):
    answer = True
    num = str(x)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])

    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer


# 다른 사람의 풀이
def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0
