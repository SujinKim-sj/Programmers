def solution(d, budget):
    answer = 0
    d.sort()

    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break

    return answer
