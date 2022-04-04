# 풀이(1) - numpy 사용
import numpy as np


def solution(arr1, arr2):
    answer = [[]]
    answer = np.array(arr1) + np.array(arr2)

    return answer.tolist()
  
# 풀이(2) - for문 사용
def solution2(arr1, arr2):
    answer = arr1
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] += arr2[i][j]

    return answer
