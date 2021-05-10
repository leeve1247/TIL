def solution(s):
    length = len(s)
    answer = ""
    if length%2 == 0:
        t=length//2
        answer = s[t-1:t+1]
    else:
        answer = s[length//2]
    return answer