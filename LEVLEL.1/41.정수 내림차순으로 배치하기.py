def solution(n): #n을 int로 변환해줘야 한다. 
    ls = list(str(int(n)))
    ls.sort(reverse=True)
    return int(''.join(ls))
print(solution(118372))
