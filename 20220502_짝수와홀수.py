# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

# 다른 사람의 풀이
def evenOrOdd(num):
    return "Even" if num%2 == 0 else "Odd"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))