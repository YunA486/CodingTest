# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

def solution(n):
    answer = ''
    ma = list(map(int,str(n)))
    ma.sort(reverse=True)
    for i in ma:
        answer += str(i)
    return int(answer)

# 다른 사람의 풀이

# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))