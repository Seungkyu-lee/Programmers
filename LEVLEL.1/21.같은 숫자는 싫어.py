# def solution(arr):
#     answer = []
#     for i in range(len(arr)):
#         if [arr[i]] == arr[i + 1:i + 2]:
#             continue
#         answer.append(arr[i])
#
#     return answer

def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]:
            continue
        a.append(i)
    return a


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
