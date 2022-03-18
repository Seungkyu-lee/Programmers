def solution(n):

    ans = int(n)**0.5
    if ans == int(ans):
        return int((ans+1)**2)
    else:
        return -1

print(solution(121))
print(solution(3))