number = "999"
k = 2
answer =''
lisnumber = []
for i in number:
    lisnumber.append(int(i))
while True:
    if k == 0 or lisnumber==[]:
        for i in lisnumber:
            answer += str(i)
        break
    #가장 큰 수 고르기
    n=len(lisnumber)
    pnum = max(lisnumber[:k+1])
    print(lisnumber,k)

    #반영하기
    answer += str(pnum)

    #가장 큰 수 포함 숫자들 제거
    tem = lisnumber.index(pnum)
    lisnumber = lisnumber[tem+1:]
    print(lisnumber,k,tem)
    #제거한 숫자만큼 K값 감소
    k -= tem
print(answer)