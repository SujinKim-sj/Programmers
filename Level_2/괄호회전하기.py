# 월간 코드 챌린지 시즌2 - Lv2. 괄호 회전하기

def solution(s):
    s2 = list(s)
    answer = 0

    for _ in range(len(s)):
        stack = []
        for i in range(len(s2)):
            if len(stack) > 0:
                if stack[-1] == '[' and s2[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and s2[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and s2[i] == '}':
                    stack.pop()
                else:
                    stack.append(s2[i])
            else:
                stack.append(s2[i])
        # print("for문 end")

        # 스택이 비어있으면 올바른 괄호
        if len(stack) == 0:
            answer += 1

        # 왼쪽으로 x칸만큼 회전
        s2.append(s2.pop(0))

    return answer