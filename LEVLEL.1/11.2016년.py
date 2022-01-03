import datetime


def getDayName(a, b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    t = ['MON', 'TUE', 'WED', 'FRI', 'SAT', 'SUN']
    print(datetime.date(2016, a, b).weekday())
    return t[datetime.datetime(2016, a, b).weekday()]


# 아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5, 24))

import calendar

print(calendar.calendar(2022))
print(calendar.prmonth(2021,12))
