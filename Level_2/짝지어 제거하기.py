def solution(s):
    answer = 0
    arr = []

    for i in range(len(s)):
        if len(arr) == 0:
            arr.append(s[i])
        elif arr[-1] == s[i]:
            arr.pop()
        else:
            arr.append(s[i])

    if len(arr) == 0:
        answer = 1

    return answer