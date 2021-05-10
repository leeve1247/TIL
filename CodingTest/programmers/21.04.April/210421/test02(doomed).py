def solution(k, room_number):
    booked_rooms = []
    for guest in room_number:
        booked = False
        count = 0
        while booked == False:
            if guest + count in booked_rooms:
                count = count + 1
            else :
                booked_rooms.append(guest + count)
                booked = True
    return booked_rooms