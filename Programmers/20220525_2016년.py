# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.
# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

import datetime as dt

def solution(a, b):
    d = dt.datetime(2016,a,b)
    answer = d.weekday()
    if answer == 0:
        return 'MON'
    elif answer == 1:
        return 'TUE'
    elif answer == 2:
        return 'WED'
    elif answer == 3:
        return 'THU'
    elif answer == 4:
        return 'FRI'
    elif answer == 5:
        return 'SAT'
    elif answer == 6:
        return 'SUN'

# 다른 사람의 풀이
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))