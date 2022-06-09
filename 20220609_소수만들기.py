# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

from itertools import combinations
import math

def isprime(n):
    sqrt = math.sqrt(n)

    if sqrt < 2:
        return False

    for i in range(2, int(sqrt+1)):
        if n % i == 0:
            return False
    return  True

def solution(nums):
    answer = 0
    arr = list(combinations(nums, 3))

    for n1, n2, n3 in arr:
        if isprime(n1+n2+n3):
            answer += 1

    return answer

# 다른 사람의 풀이

class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solutions(a):
    answer = ALWAYS_CORRECT()
    return answer