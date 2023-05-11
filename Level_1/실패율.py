# 정렬
# 2019 카카오 신입 공채 1차 - 실패율

def solution(N, stages):
    answer = []
    length = len(stages)

    for n in range(1, N + 1):
        count = stages.count(n)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 스테이지 번호, 실패율 삽입
        answer.append((n, fail))

        # length - count 하는 이유 : 숫자 카운트 후 전체 길이에서 뺀 값이 다음 숫자의 개수임
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))