def solution(s):

    return " ".join(["".join([w.upper() if i%2 == 0 else w.lower() for i, w in enumerate(a)])for a in s.split(" ")])


print(solution("try hello world"))