#https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3
#이진탐색문제?
def arrivOffice(timetable,contime,buses):
    isdone = False
    iscongone = False
    
    n,i =0,0
    seats=buses[n][1]
    
    while True:
        if i == len(timetable):
            if not iscongone:
                print(contime,"con")
            break
        
        #맨 처음부터 중간에 콘이 탈 경우
        if timetable[i] > contime and not iscongone :
            passenger = contime
            iscongone = True
            print(passenger,"con")
            
        else:
            passenger = timetable[i]
            print(passenger,"crew")
            i+=1
            
        seats -= 1
        
        
        
            
    return 0

def strtohours(time):
    temp =time.split(":")
    hours = int(temp[0])
    minutes = int(temp[1])
    return 60*(hours-9) + minutes

def solution(n, t, m, timetable):
    #배차 버스생성
    buses = []
    for i in range(0,n):
        buses.append([i*t,m])
    print("버스들",buses)
    
    for i in reversed(range(len(timetable))):
        temp = strtohours(timetable[i])
        if temp > buses[-1][0]:
            timetable.pop(i)
        else:
            timetable[i] = temp

    timetable.sort()
    print("유효 친구들",timetable)
    
    contime = 0
    arrivOffice(timetable,contime,buses)
    answer = ''
    return answer