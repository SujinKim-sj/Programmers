# 연습문제 - Lv2. 다음 큰 숫자

def solution(n):
    binary_n = bin(n)
    answer = n + 1

    # 1의 개수
    one_count = binary_n.count('1')

    while (True):
        if bin(answer).count('1') == one_count:
            return answer
        else:
            answer += 1
