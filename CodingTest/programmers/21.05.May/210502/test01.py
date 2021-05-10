def solution(clothes):
    dicClothes = {}
    for wearable in clothes:
        if dicClothes.get(wearable[1]) == None:
            dicClothes[wearable[1]] = 2
        else:
            dicClothes[wearable[1]] += 1
    temp = dicClothes.values()
    answer = 1
    for i in temp:
        answer *= i
    answer -= 1
    return answer