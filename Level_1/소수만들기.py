from itertools import combinations


def prime(num):
    result = 0
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def solution(nums):
    answer = 0
    nums_arr = list(combinations(nums, 3))
    for i in nums_arr:
        sum = i[0] + i[1] + i[2]

        if prime(sum):
            answer += 1

    return answer


print(solution([1, 2, 7, 6, 4]))