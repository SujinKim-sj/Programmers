# 해시 Lv2. 전화번호 목록

def solution(phone_book):
    answer = True
    pb_hash = {}  # phone_book 을 담을 dictionary

    for i in phone_book:
        pb_hash[i] = 1

    for i in phone_book:
        pb_str = ""
        for j in i:
            pb_str += j
            # pb_hash 내에 pb_str 의 번호가 존재하지만 전체 번호는 다른 경우
            if pb_str in pb_hash and pb_str != i:
                answer = False

    return answer


# 다른 사람의 풀이
def solution2(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
