def solution(n, times):
    #리턴값을 정해두고 그게 최솟값인지 판단하기
    maxreturns = ((n//len(times))+1)*max(times)
    minreturns = (n//len(times))*min(times)
    def ismaxresult(n,times,thetimes):
        result = 0
        totalnum = 0
        for simsaone in times:
            totalnum += thetimes//simsaone
        #totalnum이 n보다 작다 -> thetimes를 키운다.(시간부족)
        if totalnum < n:
            result = -1
        #totalnum이 n보다 크거나 같다. -> thetimes를 줄인다.(시간 여유)
        elif totalnum >= n:
            result = 1
        return result
    answer = 0
    midreturns = minreturns+(maxreturns-minreturns)//2
    while True:
        if ismaxresult(n,times,midreturns) == 1:
            maxreturns = midreturns
            midreturns = minreturns+(maxreturns-minreturns)//2
        elif ismaxresult(n,times,midreturns) == -1:
            minreturns = midreturns
            midreturns = minreturns+(maxreturns-minreturns)//2
        if minreturns+1 == maxreturns or minreturns == maxreturns:
            answer = maxreturns
            break
    
    return answer