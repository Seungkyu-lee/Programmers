from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0],0])
    q.append([numbers[0]*(-1),0])
    while q:
        tmp, idx = q.popleft()
        idx += 1
        if idx<len(numbers):
            q.append([tmp+numbers[idx],idx])
            q.append([tmp-numbers[idx],idx])
        else:
            if target == tmp:
                answer += 1
    return answer
def solution2(numbers, target):
    n = len(numbers)
    ans = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal ans
                ans+=1
            return
        else:
            dfs(idx+1,result + numbers[idx])
            dfs(idx+1,result - numbers[idx])
    dfs(0,0)


print(solution([4, 1, 2, 1],4))
print(solution2([4, 1, 2, 1],4))