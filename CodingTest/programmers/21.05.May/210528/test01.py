def solution(n):
    #1000000 이하의 소수 목록 생성하기
    numbers = []
    for i in range(2,n+1):
        numbers.append(i)
    i = 0
    while True:
        if len(numbers) == i:
            break
        j = i+1
        while True:
            if len(numbers) <= j:
                break
            if numbers[j] % numbers[i] == 0:
                del numbers[j]
            j+=1
        # print(numbers,numbers[i])
        i += 1      
    return len(numbers)