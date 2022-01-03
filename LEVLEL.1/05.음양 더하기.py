# def solution(absolutes, signs):
#     answer = 0
#     for idx, num in enumerate(absolutes):
#         if signs[idx] == 'true':
#             answer += num
#         else:
#             answer -= num
#
#     return answer

def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))


print(solution([4, 7, 12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))

