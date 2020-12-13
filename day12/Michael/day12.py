import re
from collections import defaultdict
with open('day12/Michael/day12.txt','r') as f:
    instructions = f.read().splitlines()

cardinal = defaultdict(lambda: (0,0))
cardinal['N'] = (1,0)
cardinal['E'] = (0,1)
cardinal['S'] = (-1,0)
cardinal['W'] = (0,-1)
regex = re.compile(r"([NESWLRF])(\d+)")

cardinalList = ['N','E','S','W']
cardinalIndex = 1
coordinates = (0,0)

mult = lambda b: lambda a: a[0]+a[1]*b

def getIndex(index,step):
    if step < 0:
        step += 4
    return (index+step)%4

for instruction in instructions:
    (action,num) = regex.match(instruction).groups()
    num = int(num)
    direction = cardinal[cardinalList[cardinalIndex]]
    if action == 'R' or action == 'L':
        cardinalIndex = getIndex(cardinalIndex,(1 if action == 'R' else -1)*num//90)
        print(action,num,coordinates,direction,cardinal[cardinalList[cardinalIndex]])
    else:
        print(action,num,coordinates,direction,direction if action == 'F' else cardinal[action])
        coordinates = tuple(map(mult(num),zip(coordinates,direction if action == 'F' else cardinal[action]))) # F,N,E,S,W

print(abs(coordinates[0])+abs(coordinates[1]))

### Part 2

directions = [(1,1),(-1,1),(-1,-1),(1,-1)]
ship = (0,0)
waypoint = (1,10)

mult2 = lambda a: abs(a[0])*a[1]
swap = lambda a: (a[1],a[0])

def findIndex(waypoint):
    y,x = waypoint
    y,x = (y if y != 0 else 1,x if x != 0 else 1)
    return directions.index((y/abs(y),x/abs(x)))

for instruction in instructions:
    (action,num) = regex.match(instruction).groups()
    num = int(num)
    if action == 'R' or action == 'L':
        index = findIndex(waypoint)
        print(action,num,index,getIndex(index,(1 if action == 'R' else -1)*num//90),waypoint,tuple(map(mult2,zip(waypoint if num%180 == 0 else (waypoint[1],waypoint[0]),directions[getIndex(index,(1 if action == 'R' else -1)*num//90)]))))
        index = getIndex(index,(1 if action == 'R' else -1)*num//90)
        waypoint = tuple(map(mult2,zip(waypoint if num%180 == 0 else swap(waypoint),directions[index])))
    elif action == 'F':
        print(action,num,ship,'=>',tuple(map(mult(num),zip(ship,waypoint))))
        ship = tuple(map(mult(num),zip(ship,waypoint)))
    else:
        print(action,num,waypoint,'=>',tuple(map(mult(num),zip(waypoint,cardinal[action]))))
        waypoint = tuple(map(mult(num),zip(waypoint,cardinal[action]))) # N,E,S,W

print(abs(ship[0])+abs(ship[1]))