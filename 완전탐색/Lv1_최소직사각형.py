# 완전탐색 LV1 - 최소 직사각형

def solution(sizes):
    answer = 0
    w = []
    h = []

    # 1) 양쪽 비교 후 큰 쪽이 왼 / 오로 가게 바꾸기

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            w.append(sizes[i][1])
            h.append(sizes[i][0])
        else:
            w.append(sizes[i][0])
            h.append(sizes[i][1])

    # 2) 가로, 세로 각 배열에서 max 값 구하기
    answer = max(w) * max(h)

    return answer

# 다른 사람의 풀이
def solution2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)