# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

a = input()
a = int(a)

sum = 0

for i in range(a+1):
    sum += i
print(sum)