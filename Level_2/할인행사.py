def solution(want, number, discount):
    answer = 0
    count = []

    for i in range(len(want)):
        for j in range(number[i]):
            count.append(want[i])
    count.sort()

    for i in range(len(discount) - 9):
        ten = discount[i:i + 10]
        ten.sort()
        if count == ten:
            answer += 1

    return answer