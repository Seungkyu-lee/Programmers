def solution(s):
    i, mod = divmod(len(s), 2)
    if mod:
        answer = s[i]
    else:
        answer = s[i - 1] + s[i]
    return answer


print(solution("qwer"))
print(solution("abcde"))
