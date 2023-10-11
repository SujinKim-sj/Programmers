def solution(numbers):
    answer = [-1 for i in range(len(numbers))]
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i) # 인덱스

    return answer