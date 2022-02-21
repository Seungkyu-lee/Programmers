def solution(arr):
    arr.sort(reverse=True)
    arr.pop()
    if len(arr) == 0:
        arr = [-1]
    return arr

print(solution([4,3,2,1]))
print(solution([10]))