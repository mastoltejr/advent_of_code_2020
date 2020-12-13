import math
seats = []
with open('day11.txt','r') as f:
    for row in f:
        seats.append(list(row.replace('\n','')))

directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def validLocation(layout,row,column):
    return row >= 0 and row < len(layout) and \
        column >= 0 and column < len(layout[row])

def countAdjacent(layout,row,column,maxStep,lookFor):
    count = 0
    for (yslope,xslope) in directions:
        step = 1
        #print(yslope,xslope)
        while validLocation(layout,row+yslope*step,column+xslope*step) and step <= maxStep:
            #print(row+yslope*step,column+xslope*step,layout[row+yslope*step][column+xslope*step])
            if layout[row+yslope*step][column+xslope*step] == lookFor:
                count += 1
                break
            elif layout[row+yslope*step][column+xslope*step] == 'L':
                break
            step += 1
        #print('===============')
    return count

def compareLayouts(layout1,layout2):
    for i in range(0,len(layout1)):
        if ''.join(layout1[i]) != ''.join(layout2[i]):
            return False
    return True

def prettyPrint(layout):
    for row in layout:
        print(''.join(row))
    print('============================')

def iteration(layout,maxStep=math.inf,lookFor="#"):
    new_layout = []
    for i,row in enumerate(layout):
        new_row = []
        for j,column in enumerate(row):
            if column == 'L' and countAdjacent(layout,i,j,maxStep,lookFor) == 0:
                new_row.append('#')
            elif column == '#' and countAdjacent(layout,i,j,maxStep,lookFor) >= 5: # part1 is 4
                new_row.append('L')
            else:
                new_row.append(column)
        new_layout.append(new_row)
    return new_layout

def countSeats(layout,lookFor = '#'):
    count = 0
    for row in layout:
        for column in row:
            count += 1 if column == lookFor else 0
    return count
count = 0

prettyPrint(seats)
while count < 1000:
    new_seats = iteration(seats) # define maxStep = 1 on part1
    prettyPrint(new_seats)
    if compareLayouts(seats,new_seats):
        break
    seats = new_seats
    count += 1

print(str(count) + ' iterations')
print(countSeats(seats))