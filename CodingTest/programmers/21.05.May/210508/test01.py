def solution(s):
    answer = False
    pnum = 0
    ynum = 0
    for i in s:
        if i == "p":
            pnum += 1
        elif i == "y":
            ynum += 1
    if pnum == ynum :
        answer = True
    return answer