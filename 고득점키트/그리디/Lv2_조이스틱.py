def solution(name):
    answer = 0
    default = "A" * len(name)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    move = len(name) - 1

    for i in range(len(name)):
        if default[i] != name[i]:
            # 알파벳 맞추기
            tmp = min(alpha.index(name[i]) - alpha.index('A'), alpha.index('Z') - alpha.index(name[i]) + 1)
            answer += tmp

        # 커서 이동
        next = i + 1
        while next < len(name) and name[next] == 'A':  # 다음이 A이면 커서 이동해야함
            next += 1

        d = min(i, len(name) - next)
        move = min(move, i + len(name) - next + d)

    answer += move

    return answer