def solution(n):
    decimalist = [2]
    if n == 1:
        answer = 0
    elif n == 2:
        answer = 1
    else:
        #1 포함
        for i in range(3,n+1):
            isdecimal = True
            for decimal in decimalist:
                if i % decimal == 0:
                    isdecimal = False
                    break
            if isdecimal:
                decimalist.append(i)
        answer = len(decimalist)
    return answer