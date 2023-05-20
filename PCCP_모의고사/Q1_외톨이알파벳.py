# PCCP 모의고사 1회 - 1번. 외톨이 알파벳
from collections import Counter

def solution(input_string):
    answer = []
    count = Counter(input_string)

    for i, j in count.items():
        if j >= 2:
            idx = input_string.index(i)
            count2 = Counter(input_string[idx:idx + j])

            # 외톨이 알파벳이면
            if len(count2) != 1:
                answer.append(i)

    if len(answer) == 0:
        return "N"

    answer.sort()

    return ''.join(answer)