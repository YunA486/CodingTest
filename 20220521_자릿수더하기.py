# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)

    return answer

# 다른 사람의 풀이

def sum_digit(number):
    return sum([int(i) for i in str(number)])
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))