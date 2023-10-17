def solution(array, commands):
    answer = []

    for c in commands:
        i, j, k = c[0], c[1], c[2]
        array2 = sorted(array[i - 1:j])
        answer.append(array2[k - 1])

    return answer