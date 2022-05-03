# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
        # s가 숫자이면 True 반환, 문자이면 False 반환
    else:
        return False

# 다른 사람의 풀이
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(alpha_string46("a234"))
print(alpha_string46("1234"))