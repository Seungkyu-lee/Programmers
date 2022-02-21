def solution(phone_number):
    N = len(phone_number)-4
    answer = '*'* N + phone_number[N:]
    return answer

print(solution("01033334444"))
print(solution("027778888"))
