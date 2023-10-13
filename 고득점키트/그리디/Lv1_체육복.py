#그리디 알고리즘 Lv1. 체육복

def solution(n, lost, reserve):
    # 중복 제거
    reserveSet = set(reserve) - set(lost)
    lostSet = set(lost) - set(reserve)

    for i in reserveSet:
        if i - 1 in lostSet:
            lostSet.remove(i - 1)
        elif i + 1 in lostSet:
            lostSet.remove(i + 1)

    return n - len(lostSet)
