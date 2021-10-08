'''
p충의 q호
p-1층 1~q까지 


입력 :
갯수
층수 1층에 
호수 3호   -> 0층에 3호까지 (1+2+3) = 6
층수 2층에
호수 3호  -> 1층에 3호까지 ((1)+(1+2)+(1+2+3))

'''

import sys

def live(floor, room):
    # floor 층수 , room 호수 
    if floor == 0:
        return room 
    if room == 1:
        return 1
    number = live(floor,room-1)  + live(floor-1,room)
    return number


n = int(sys.stdin.readline())

for i in range(n):
    floor = int(sys.stdin.readline())     
    room = int(sys.stdin.readline())
    print(live(floor,room))

