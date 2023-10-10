def solution(n):
    fibo = [0 for i in range(100010)]
    fibo[0] = 0
    fibo[1] = 1

    for i in range(2, len(fibo)):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1234567

    answer = fibo[n]
    return answer