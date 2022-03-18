import math


# 유클리드 호제법
# 최대 공약수 구하기
def GCD(x,y):
    while(y):
        x,y = y,x%y
    return x

def LCM(x,y):
    return (x*y)//GCD(x,y)

def solution(n, m):
    # answer = [math.gcd(n,m), math.lcm(n,m)]

    answer = [GCD(n,m),LCM(n,m)]

    return answer

print(solution(3,12))
print(solution(10,12))