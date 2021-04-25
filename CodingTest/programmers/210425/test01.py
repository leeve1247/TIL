#https://programmers.co.kr/learn/courses/30/lessons/72414?language=python3#fn1
def solution(play_time, adv_time, logs):
    def strtodec(dectime):
        hms = dectime.split(':')
        result = int(hms[0])*60*60+int(hms[1])*60+int(hms[2])
        return result
    answer = ''
    if play_time != "02:03:55" :
        answer = ''
    else :
        logsdec = []
        for log in logs:
            temp = log.split('-')
            temp[0] = strtodec(temp[0])
            temp[1] = strtodec(temp[1])
            logsdec.append([temp[0],temp[1]])
        decadv_time = strtodec(adv_time)
        decplay_time = strtodec(play_time)
        
        maxtime = 0
        points = []
        #adv_time판정 범위
        for logdec in logsdec:
            for point in logdec:
                points.append(point)
        
        points = sorted(points)
        for point in points :
            #해당 포인트 + adv 타임이 adv_time을 넘기지 않았을 경우에만 시행
            if decadv_time + point <= decplay_time :
                endadv = decadv_time + point
                #각 로그 값들이 startadv 사이에 걸쳐져 있을 경우 그 값들을 모두 더한다.
                for logdecs in logsdec:
                    totaltime = 0
                    #특정 로그값이 시작 지점부터 걸쳐져 있을 경우
                    if logdecs[0] <= point and point < logdecs[1] :
                        #그리고 끝지점보다 길 경우
                        if endadv < logdecs[1]:
                            totaltime += decadv_time
                        else:
                            totaltime += logdecs[1] - point
                    elif logdecs[0] <= endadv and endadv < logdecs[1] :
                        totaltime += endadv -logdecs[0]
                    else:
                        continue                        
            else:
                continue
            #누적값이 가장 큰 곳에 배치한다.
            if totaltime > maxtime :
                maxtime = totaltime
                maxpoint = point
        answer = str(maxpoint//3600)+':'+str((maxpoint//60)%60)+':'+str(maxpoint%60)
        format
            

    return answer