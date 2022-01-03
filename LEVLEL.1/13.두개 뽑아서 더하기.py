from itertools import combinations
def solution(numbers):
    answer = []
    cb = combinations(numbers, 2)
    for i, j in cb:
        answer.append(i + j)
    answer = sorted(list(set(answer)))
    return answer

print(solution([2,1,3,4,1]))