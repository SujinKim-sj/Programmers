# 구현, 완전탐색
# 2020 카카오 신입 공채 - 문자열 압축

s = input()
answer = len(s)

# 1개 단위(step)부터 압축 단위를 늘려가며 확인
for step in range(1, len(s) // 2 + 1):
    compressed = ""
    prev = s[0:step]    # 앞에서부터 step 만큼의 문자열 추출
    count = 1

    # 단위만큼 증가시키며 이전 문자열과 비교
    for j in range(step, len(s), step):
        print("prev", prev)
        # 이전 상태와 동일하면 압축 횟수 증가
        if prev == s[j:j + step]:
            count += 1
        else:   # 다른 문자열이 나왔다면
            compressed += str(count) + prev if count >= 2 else prev
            prev = s[j:j + step]    # 다시 상태 초기화
            count = 1
    # 남아있는 문자열에 대해 처리
    compressed += str(count) + prev if count >= 2 else prev
    answer = min(answer, len(compressed))

print(answer)