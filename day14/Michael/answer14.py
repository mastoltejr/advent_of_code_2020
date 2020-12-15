from collections import defaultdict
import re

def maskRules(mask, ignore = 'X'):
    return [(i,m) for i,m in enumerate(mask) if m != ignore]

def applyRules(mask_rules,binary):
    for i,m in mask_rules:
            binary = binary[:i] + m + binary[(i+1):]
    return binary

def toBinary(num):
    if num == 0:
        return ''
    return str(int(num)%2) + str(toBinary(int(num)//2))

def toBinaryString(num,size=36):
    dec = toBinary(num)
    return '0'*(size-len(dec))+dec[::-1]


def toDecimal(dec):
    dec = dec.lstrip('0')[::-1]
    total = 0
    for i,digit in enumerate(dec):
        total += 2**i if digit == '1' else 0
    return total

def getAddressOptions(mask,address):
    mask_rules = maskRules(mask,ignore = '0')
    address = toBinaryString(address)
    address = applyRules(mask_rules,address)
    address_options = []
    tail = [address]
    while len(tail) > 0:
        head, *tail = tail
        if head.count('X') == 1:
            address_options.append(head.replace('X','0'))
            address_options.append(head.replace('X','1'))
        else:
            tail.append(head.replace('X','0',1))
            tail.append(head.replace('X','1',1))
    return address_options



with open('day14/Michael/day14.txt','r') as f:
    instructions = f.read().splitlines()

memory = defaultdict(lambda: 0)
memory2 = defaultdict(lambda: 0)
mask_regex = re.compile(r"mask = (\w+)",re.IGNORECASE)
ins_regex = re.compile(r"mem\[(\d+)\] = (\d+)",re.IGNORECASE)
mask_rules = []

for instruction in instructions:
    valid_mask = mask_regex.search(instruction)
    ins_keys = ins_regex.match(instruction)
    if valid_mask:
        mask = valid_mask.groups()[0]
        mask_rules = maskRules(mask)
    elif ins_keys:
        (index,num) = ins_keys.groups()
        #print(index,num)
        memory[index] = toDecimal(applyRules(mask_rules,toBinaryString(num)))
        for option in getAddressOptions(mask,index):
            #print(index,'=>',toDecimal(option))
            memory2[toDecimal(option)] = int(num)
    #print('===============')

total = 0
for j in memory.values():
    total += j
print(total)
total = 0
for j in memory2.values():
    total += j
print(total)