# 완전탐색 LV2 - 카펫

def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = yellow // i
            h = i
            if (w + h) * 2 + 4 == brown and w >= h:
                answer.append(w + 2)
                answer.append(h + 2)

    return answer
