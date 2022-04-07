# 유클리드 호제법 사용
def gcd(n, m):
    if m % n != 0:
        m, n = n, m % n
        return gcd(n, m)
    else:   # m % n == 0 일 때
        return n


def solution(n, m):
    return [gcd(n, m), int(n * m / gcd(n, m))]


print(solution(3, 12))