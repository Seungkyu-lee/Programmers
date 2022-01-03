def solution(a, b):
    if a > b:
        a, b = b, a
    answer = sum(range(a, b + 1))
    return answer


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
