from itertools import permutations
import math

# 소수 찾기
# 제곱근 까지만 확인하면 된다
def primeNumber(number):
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0: # 나눠 떨어지는 숫자가 있으면 소수가 아님
            return False
    return True     # 전부 나눠 떨어지지 않는다면 소수



######
numbers = "17"
n = len(numbers)

# 1) 문자열의 숫자 분리
nums = [n for n in numbers]
per = []  # 순열
answer = set()

# 2) 순열로 만들수 있는 모든 숫자 만들기
for i in range(1, n + 1):
    per += list(permutations(nums, i))

# 3) 숫자로 변환
per_nums = [int("".join(p)) for p in per]
arr = [True for i in range(len(per_nums) + 1)]

for p in per_nums:
    if p < 2:
        continue
    for i in range(2, int(math.sqrt(p)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= p:
                arr[i * j] = False
                j += 1

# 4) set으로 중복 제거 후 반환
print(arr)



from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)