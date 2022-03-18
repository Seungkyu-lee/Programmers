def collatz(num,ans):
    n = num
    while n >= 1:
        if ans >= 500:
            return -1
        if n == 1:
            return ans
        elif n % 2 == 0:
            ans += 1
            n = n // 2
        elif n % 2 == 1:
            ans += 1
            n=n * 3 + 1


def solution(num):
    answer = 0
    n = num
    ans=collatz(n, answer)
    return ans

print(solution(6))
print(solution(16))
print(solution(626331))