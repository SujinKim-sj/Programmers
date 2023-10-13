def solution(number, k):
    answer = ''
    stack = []

    for i in number:
        if len(stack) == 0:
            stack.append(i)
            continue
        if k > 0:
            while stack[-1] < i:
                stack.pop()
                k -= 1

                if not stack or k <= 0:
                    break
        stack.append(i)

    answer = ''.join(stack[:len(number) - k])

    return answer


number = input()
k = int(input())
print(solution(number, k))