room_number = [1,3,4,1,3,1]

booked_rooms = [[room_number[0],room_number[0]]]
result = [room_number[0]]
room_number = room_number[1:]

def makeout(list1):
    a = 0
    while a < len(list1)-1:
        if list1[a][1] + 1 == list1[a+1][0] :
            list1[a][1] = list1[a+1][1]
            del list1[a+1]
            a = a-1
        a = a + 1
    return list1

def insertguest(guest, booked_rooms,result):
    a = 0
    thelength = len(booked_rooms)
    booked_rooms = makeout(booked_rooms)
    while a < thelength:
        if guest < booked_rooms[a][0]:
            booked_rooms.insert(a,[guest,guest])
            result.append(guest)
            break
        elif booked_rooms[a][0] <= guest and guest <= booked_rooms[a][1]:
            booked_rooms[a][1] = booked_rooms[a][1]+1
            result.append(booked_rooms[a][1])
            break
        elif booked_rooms[a][1] < guest and a == thelength-1:
            booked_rooms.append([guest,guest])
            result.append(guest)
            break
        else:
            a = a + 1
            continue
    return(booked_rooms)
for guest in room_number :
    booked_rooms=makeout(booked_rooms)
    booked_rooms=insertguest(guest,booked_rooms,result)
print(result)
