# 스택/큐 - Lv1. 같은 숫자는 싫어
def solution(arr):
    answer = []

    for i in range(len(arr)):
        if len(answer) > 0:
            if answer[-1] == arr[i]:
                answer.pop()
                answer.append(arr[i])
            else:
                answer.append(arr[i])

        else:
            answer.append(arr[i])

    return answer