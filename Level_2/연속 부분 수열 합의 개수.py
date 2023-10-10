def solution(elements):
    answer = 0
    sumArr = set()
    length = len(elements)
    elements = elements * 2  # 원형 수열

    for i in range(length):
        for j in range(length):
            print(i, j, j + i + 1)
            sumArr.add(sum(elements[j:j + i + 1]))

    answer = len(sumArr)
    return answer