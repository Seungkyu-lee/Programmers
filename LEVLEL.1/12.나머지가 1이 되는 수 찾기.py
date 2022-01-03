def solution(n):
    answer = 0
    for x in range(1, n + 1):
        if n % x == 1:
            answer = x
            break
    return answer


print(solution(10))
print(solution(12))
