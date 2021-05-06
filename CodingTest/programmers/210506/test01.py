#판만들기
def makekeypan(key,panlen,locklen,keylen):
    pan = []
    for i in range(panlen):
        pan.append([])
        for j in range(panlen):
            if locklen-1 <= i and i <= locklen+keylen-2 and locklen-1 <= j and j <= locklen+keylen-2:
                pan[i].append(key[i+1-locklen][j+1-locklen])
            else:
                pan[i].append(".")
    return pan

#반시계방향 회전
def rotate(lock,locklen):
    temp = []
    for i in range(locklen):
        temp.append([])
        for j in range(locklen):
            temp[i].append(lock[j][locklen-1-i])
    return temp
    
#자물쇠와 판(키를 넣은) 합치고 체크하기
#체크해서 통과할 경우는 lock 부분이 모두 1일 때임
def insert(pan,lock,panlen,locklen,row,col):
    isunlocked = False
    cannotunlocked = False
    count = 0
    utemp = None
    
    for i in range(panlen):
        if cannotunlocked :
            break
        for j in range(panlen):
            if row <= i and i <= row+locklen-1 and col <= j and j <= col+locklen-1:
                if pan[i][j] == ".":
                    utemp = lock[i-row][j-col]
                else:
                    utemp = pan[i][j] + lock[i-row][j-col]
                    
                #판정
                if utemp == 1:
                    count += 1
                elif utemp == 0 or utemp == 2 :
                    cannotunlocked = True
                    break
    if count == locklen**2:
        isunlocked = True
    return isunlocked
                       

    

def solution(key, lock):
    answer = False
    
    
    locklen = len(lock)
    keylen = len(key)
    panlen = keylen + 2*locklen - 2
    #판을 만든다.
    pan = makekeypan(key,panlen,locklen,keylen)
    
    #row,col을 각각 locklen + keylen -1까지 진행하면서 자물쇠를 한번씩 돌려가면서 끼워보기
    for i in range(locklen + keylen -1):
        if answer == True:
            break
        for j in range(locklen + keylen -1):
            if insert(pan,lock,panlen,locklen,i,j):
                answer = True
                print(i,j,"0회전")
                break
            lock = rotate(lock,locklen)
            if insert(pan,lock,panlen,locklen,i,j):
                answer = True
                print(i,j,"1회전")
                break
            lock = rotate(lock,locklen)
            if insert(pan,lock,panlen,locklen,i,j):
                answer = True
                print(i,j,"2회전")
                break
            lock = rotate(lock,locklen)
            if insert(pan,lock,panlen,locklen,i,j):
                answer = True
                print(i,j,"3회전")
                break
            lock = rotate(lock,locklen)


    return answer