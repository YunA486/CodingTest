# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

a, b = input().split()
a, b = int(a), int(b)

num = list(map(int, str(b)))

print(num[2]*a)
print(num[1]*a)
print(num[0]*a)

# --------------------------------------------

A = int(input())

B = input()

print(A * int(B[2]))

print(A * int(B[1]))

print(A * int(B[0]))

print(A * int(B))