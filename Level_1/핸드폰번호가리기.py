# 풀이(1) - 나의 풀이
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) - 4):
        answer += '*'

    answer += phone_number[-4:]
    return answer

# 풀이(2) - 다른 사람의 풀이
def solution2(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]
