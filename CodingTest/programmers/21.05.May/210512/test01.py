def makearr(n,arr):
    answer = []
    for i in range(len(arr)):
        answer.append([])
        temp = arr[i]
        while True:
            if temp <= 0:
                break
            answer[i].insert(0,temp%2)
            temp = temp//2
        if len(answer[i]) < n:
            while True:
                if len(answer[i]) == n:
                    break
                answer[i].insert(0,0)
    return answer

def solution(n, arr1, arr2):
    answer= []
    arr1 = makearr(n,arr1) 
    arr2 = makearr(n,arr2)
    for i in range(n):
        answer.append("")
        for j in range(len(arr1[0])):
            if arr1[i][j] == 1 or arr2[i][j] == 1:
                   answer[i] +="#"
            else:
                   answer[i] += " "
    return answer