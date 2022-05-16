# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

def solution(arr):
    cnt = 1000000
    for i in arr:
        if i < cnt:
            cnt = i
    if cnt == 10 and len(arr) == 1:
        return [-1]
    else:
        arr.remove(cnt)

    return arr

# 다른 사람의 풀이
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4,3,2,1]
print("결과 {} ".format(rm_small(my_list)))