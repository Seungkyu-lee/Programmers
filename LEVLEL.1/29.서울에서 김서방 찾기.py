def solution(seoul):
    # for i, s in enumerate(seoul):
    #     if s == 'Kim':
    #         answer = i
    #
    # return '김서방은 {}에 있다'.format(answer)
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


print(solution(["Jane", "Kim"]))
