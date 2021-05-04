# 나만의 변환하기 놀이
#"()"를 새로운 문자열 위치에 배열 후, "(" 이걸 넣은다음 다음 공란에서 ")"이거 넣기
def initialize(p,plis,anlis):
    for i in range(len(p)):
        plis.append([p[i],i])
        anlis.append("")
    return plis

def delete(plis,anlis):
    temp = []
    for i in range(len(plis)-1):
        if plis[i][0] == "(" and plis[i+1][0] == ")":
            anlis[plis[i][1]] = "("
            anlis[plis[i+1][1]] = ")"
            temp.append(i)
            temp.append(i+1)
    for i in reversed(temp):
        plis.pop(i)
    return 0
def change(plis):
    for i in range(len(plis)-1):
        if plis[i][0] == ")" and plis[i+1][0] == "(":
            plis[i][0] = "("
            plis[i+1][0] = ")"
            #break 하지 않으면 ))(( -> )()( -> )(() 해버리는 불상사가 발생함
            break
def solution(p):
    anlis = []
    plis = []
    initialize(p,plis,anlis)
    while True:
        if plis == []:
            break
        delete(plis,anlis)
        change(plis)
    answer = ""
    for i in anlis:
        answer += i
    return answer