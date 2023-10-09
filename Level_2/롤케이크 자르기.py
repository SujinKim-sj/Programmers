from collections import Counter

def solution(topping):
    answer = 0
    chul = Counter(topping)
    bro = set()

    for i in topping:
        chul[i] -= 1
        bro.add(i)

        if chul[i] == 0:
            del chul[i]

        if len(chul.keys()) == len(bro):
            answer += 1

    return answer