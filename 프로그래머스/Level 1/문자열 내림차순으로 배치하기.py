//https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3
//문자열에 sorted를 하면 리스트로 된다.
def solution(s):
    return ''.join(sorted(s, reverse=True))
