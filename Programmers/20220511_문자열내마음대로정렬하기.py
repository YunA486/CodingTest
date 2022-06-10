# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
# 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):
    answer = []
    answers = []
    for i in strings:
        answers.append(i[n]+i)
    answers.sort()
    for i in answers:
        answer.append(i[1:])
    return answer

# 다른 사람의 풀이
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))