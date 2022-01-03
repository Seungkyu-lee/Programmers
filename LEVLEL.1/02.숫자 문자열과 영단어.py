dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
       "eight": "8", "nine": "9"}


def solution(s):
    answer = s
    for k, v in dic.items():
        answer = answer.replace(k, v)
    return int(answer)


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

''' 
    문자열은 .replace(old, new)를 사용해서 바꿔 줄 수 있다.
'''
