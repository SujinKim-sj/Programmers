# 2020 카카오 신입 공채 LV2 - 괄호 변환

# 균형잡인 괄호 인덱스 반환
def balanced_index(p):
    count = 0    # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


# 올바른 괄호 문자열인지 판단
def check(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1

    return True     # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer

    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    # 올바른 괄호 문자열이라면 아래의 과정 수행
    if check(u):
        answer = u + solution(v)
    else:   # 올바른 괄호 문자열이 아니라면 아래의 과정 수행
        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1 : -1])     # 첫번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)

    return answer