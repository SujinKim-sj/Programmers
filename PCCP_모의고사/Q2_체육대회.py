# PCCP 모의고사 1회 - 2번. 체육대회

import itertools

def solution(ability):
    answer = 0

    student = len(ability)  # 학생 수
    event = len(ability[0])  # 종목 수

    arr = itertools.permutations([i for i in range(student)], event)

    for i in arr:
        sum = 0
        idx = 0
        for j in i:
            sum += ability[j][idx]
            idx += 1
        if sum > answer:
            answer = sum

    return answer