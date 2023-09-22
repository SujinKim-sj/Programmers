def solution(k, tangerine):
    answer = 0
    cnt = [0 for i in range(10000010)]

    for i in tangerine:
        cnt[i] += 1

    cnt.sort(reverse=True)

    for i in range(len(tangerine)):
        k -= cnt[i]
        answer += 1

        if k <= 0:
            break

    return answer