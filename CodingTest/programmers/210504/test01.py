#https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3#

#문자열 나누기
def dividing(s,num):
    lis = []
    tempstr = ""
    for i in range(len(s)):
        tempstr += s[i]
        if (i+1)%num == 0:
            lis.append(tempstr)
            tempstr = ""
        else:
            continue
    if tempstr != "" :
        lis.append(tempstr)
    return lis

#문자열 압축하기
def archinize(lis):
    count = 0
    temp = "-"
    result = ""
    for i in lis:
        if temp != i:
            if temp != '-':
                if count != 0:
                    result += str(count+1) + str(temp)
                else:
                    result += str(temp)
            temp = i
            count = 0
        else:
            count += 1
    if count != 0:
        result += str(count+1) + str(temp)
    else :
        result += str(temp)
    return result

def solution(s):
    if len(s) == 1:
        answer = 1
    else:
        #문자열 자르기
        gatsu = []
        n = 1
        #n개로 자르기, N의 갯수는 (len(s)/2 까지,)
        while n <= len(s)//2:
            lis = dividing(s,n)
            gatsu.append(len(archinize(lis)))
            n += 1
        answer = min(gatsu)
        
    return answer