def lcm(a, b):
    l = a * b
    while b % a != 0:
        r = b % a
        b = a
        a = r

    l //= a
    return l

def solution(arr):
    answer = lcm(arr[0], arr[1])
    tmp = 0
    for i in range(2, len(arr)):
        tmp = lcm(answer, arr[i])
        answer = tmp

    return answer
