# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    answer = []
    a = 10
    for i in arr:
        if i != a:
            answer.append(i)
            a = i
    return answer