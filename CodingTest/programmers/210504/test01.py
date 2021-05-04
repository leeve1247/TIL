def solution(s):
    def dividing(s,num):
        lis = []
        tempstr = ""
        for i in range(len(s)):
            tempstr += s[i]
            if i%num == 0:
                lis.append(tempstr)
                tempstr = ""
            else:
                continue
        print(lis)
        return lis
    
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
        result += str(count+1) + str(temp)
        return result
      
    
    
    if s == "aabbaccc":
        #1개로 자르기
        # lis = list(s)
        lis = dividing(s,2)
        result = archinize(lis)
        print(result)
        
    else :
        print("진행안함")
    answer = 0
    return answer