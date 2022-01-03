def solution(strings, n):
    # strings.sort()
    # strings.sort(key=lambda x: x[n])
    # return strings
    answer = sorted(sorted(strings), key=lambda x: x[n])
    return answer


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))
