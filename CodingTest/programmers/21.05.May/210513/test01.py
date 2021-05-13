def updatedistance(sdf1,start,edge):
    for i in edge:
        if i[0] == start:
            #i[1]은 i[0]에서 한칸 떨어져 있다.
            temp = sdf1[start] + 1
            if temp < sdf1[i[1]]:
                sdf1[i[1]] = temp
        elif i[1] == start:
            temp = sdf1[start] + 1
            if temp < sdf1[i[0]]:
                sdf1[i[0]] = temp
    return 0

def findmin(sdf1,undecided):
    minv = int(1e9)+1
    mink = -1
    for i in undecided:
        if sdf1[i] < minv:
            minv = sdf1[i]
            mink = i
    return mink

def solution(n, edge):
    undecided = []
    sdf1 = {}
    for i in range(n):
        undecided.append(i+1)
        sdf1[i+1] = int(1e9)
    
    
    sdf1[1] = 0 

    
    while True:
        if undecided == []:
            break
        start = findmin(sdf1,undecided)
        updatedistance(sdf1,start,edge)
        undecided.remove(start)
    
    themax=max(sdf1[i] for i in sdf1 if sdf1[i] != int(1e9))
    count = 0
    for i in sdf1:
        if sdf1[i] == themax:
            count += 1
    return count