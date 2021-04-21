def solution(k, room_number):
    # union & find 기법
    booked_room = {}
    result = []
    for guest in room_number :
        node = booked_room.get(guest,0)
        if node == 0:
            booked_room[guest] = guest + 1

            result.append(guest)
        else :
            keys = [guest]
            while True:
                keys.append(node)
                node = booked_room.get(node,0)
                if node == 0:
                    for key in keys:
                        booked_room[key] = keys[-1] + 1
                    result.append(keys[-1])
                    break
    return result
                

print(result)
