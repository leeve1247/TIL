#https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):
    answer = 0
    for i , v in enumerate(signs):
        if v == False:
            answer = answer - absolutes[i]
        else :
            answer = answer + absolutes[i]
    return answer