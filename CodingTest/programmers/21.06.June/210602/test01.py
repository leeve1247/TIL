#https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3
#스택 문제
def solution(s):
    strings = []
    for i in s :
        if len(strings) != 0:
            if strings[-1] == i:
                del strings[-1]
            else:
                strings.append(i)
        else:
            strings.append(i)
    if len(strings) == 0:
        answer = 1
    else:
        answer = 0
        
    return answer