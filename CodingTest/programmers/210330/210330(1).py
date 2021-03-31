numbers = [1,3,4,5,6,7,8,9]
leftHand = 10 # 10은 * 을 의미
rightHand = 12 # 12 는 # 을 의미
i = 0
answer = ""
lenth = len(numbers)
while lenth > 0 :
    curNum = numbers[i]
    if curNum == 1 or curNum == 4 or curNum == 7 :
        answer += 'L'
        leftHand = curNum
    elif curNum == 3 or curNum == 6 or curNum == 9:
        answer += 'R'
        rightHand = curNum
    elif curNum == 2:
        # 우선순위는 (1,3,5),(4,6,8),(7,0,9),(*,#)
        if leftHand in [1,3,5] :
            leftRank = 1
        elif leftHand in [4,6,8] :
            leftRank = 2
        elif leftHand in [7,0,9] :
            leftRank = 3
        elif leftHand in [10,12] :
            leftRank = 4          
        else :
            lefRank = 0
        if rightHand in [1,3,5] :
            rightRank = 1
        elif rightHand in [4,6,8] :
            rightRank = 2
        elif rightHand in [7,0,9] :
            rightRank = 3
        elif rightHand in [10,12] :
            rightRank = 4
        else :
            rightRank = 0
        if leftRank > rightRank :  #왼손보다 오른손이 가까우면
            answer += "R"
            rightHand = curNum
        elif leftRank < rightRank :  #오른손보다 왼손이 가까우면
            answer += "L"
            leftHand = curNum
        else : #같으면
            if hand == "left" :
                answer += "L"
                leftHand = curNum
            else :
                answer += "R"
                rightHand = curNum
    elif curNum == "5":
        # 우선순위는 (2,4,6,8),(1,3,7,9,0),(*,#)
        if leftHand in [2,4,6,8] :
            leftRank = 1
        elif leftHand in [1,3,7,9,0] :
            leftRank = 2
        elif leftHand in [10,12] :
            leftRank = 3
        else :
            lefRank = 0
        if rightHand in [2,4,6,8] :
            rightRank = 1
        elif rightHand in [1,3,7,9,0] :
            rightRank = 2
        elif rightHand in [10,12] :
            rightRank = 3
        else :
            rightRank = 0
        if leftRank > rightRank :  #왼손보다 오른손이 가까우면
            answer += "R"
            rightHand = curNum
        elif leftRank < rightRank :  #오른손보다 왼손이 가까우면
            answer += "L"
            leftHand = curNum
        else : #같으면
            if hand == "left" :
                answer += "L"
                leftHand = curNum
            else :
                answer += "R"
                rightHand = curNum
    elif curNum == "8":
        # 우선 순위는 (5,7,9,0),(4,6,*,#),(1,3)
        if leftHand in [5,7,9,0] :
            leftRank = 1
        elif leftHand in [4,6,10,12] :
            leftRank = 2
        elif leftHand in [1,3] :
            leftRank = 3
        else :
            lefRank = 0
        if rightHand in [5,7,9,0] :
            rightRank = 1
        elif rightHand in [4,6,10,12] :
            rightRank = 2
        elif rightHand in [1,3] :
            rightRank = 3
        else :
            rightRank = 0
        if leftRank > rightRank :  #왼손보다 오른손이 가까우면
            answer += "R"
            rightHand = curNum
        elif leftRank < rightRank :  #오른손보다 왼손이 가까우면
            answer += "L"
            leftHand = curNum
        else : #같으면
            if hand == "left" :
                answer += "L"
                leftHand = curNum
            else :
                answer += "R"
                rightHand = curNum
    elif curNum == "0":
        # 우선 순위는 (10,8,12),(7,5,9),(1,3)

    i = i + 1
    lenth = lenth - 1

print(answer)