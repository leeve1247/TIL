#https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ""
    while n > 0:
        namerji = n%3
        if namerji == 0 :
            answer = '4' + answer
            n = (n //3) - 1
        else:
            answer =  str(namerji) + answer
            n = n //3                 
    return answer