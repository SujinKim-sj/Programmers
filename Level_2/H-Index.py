# 정렬 - Lv2. H-Index

def solution(citations):
    answer = 0
    citations = sorted(citations)
    c_len = len(citations)
    for i in range(c_len):
        if citations[i] >= c_len - i:
            return c_len - i
    return answer
