# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

cnt = int(input())

for i in range(cnt):
    result1, result2 = input().split()
    result1, result2 = int(result1), int(result2)

    print(result1 + result2)