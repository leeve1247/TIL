#https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

def solution(bridge_length, weight, truck_weights):
    if bridge_length == 2:
        #다리 무게 제한이 없는 경우
        answer = []
        #0초 경과
        onbridge = []
        ontotalweight = 0
    
    
        #1초 경과
        onbridge.append([truck_weights[0],1])
        ontotalweight = truck_weights.pop(0)

        time = 1
        print(onbridge,ontotalweight,time)

        while time <= 2:
            if onbridge[0][1] == weight:
                onbridge.pop(0)
                ontotalweight -= onbridge[0][0]
            if ontotalweight + truck_weights[0] <= weight:
                print(ontotalweight, truck_weights[0])
                onbridge.append([truck_weights[0],0])
                ontotalweight += truck_weights.pop(0)
            for ontruck in onbridge:
                tem1 = ontruck[0]
                tem2 = ontruck[1]
                print(onbridge)
            
            print(onbridge,ontotalweight,time)
            time += 1
            
    time = 0

    return time