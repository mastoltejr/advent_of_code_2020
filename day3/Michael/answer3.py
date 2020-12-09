def findTree(trees,x,lookFor = '#'):
    s = trees*((x//len(trees))+1)
    found = s[x-1] == lookFor
    #print(s[:(x-1)]+('X' if found else 'O'))
    return found

def treesBySlope(left_increment, down_increment):
    left = 1
    down = 0
    tree_count = 0
    with open('day3.txt','r') as f:
        rows = f.read().splitlines()
        for row in rows:
            if down%down_increment == 0 and down > 0:
                left += left_increment
                tree_count += 1 if findTree(row,left) else 0
            # else:
            #     print('='*len(row)*(max(1,left//len(row))))
            down += 1
    return tree_count

print(treesBySlope(1,1))
print(treesBySlope(3,1))
print(treesBySlope(5,1))
print(treesBySlope(7,1))
print(treesBySlope(1,2))