def solution(s):
    answer = False

    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True

    return answer


print(solution("a234"))
print(solution("1234"))
