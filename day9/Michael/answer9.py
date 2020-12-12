from collections import defaultdict

with open('day9.txt','r') as f:
    numbers = f.read().splitlines()


def xmasSearch(numbers,preamble = 25):
    for index in range(preamble,len(numbers)):
        sumTo = int(numbers[index])
        obj = defaultdict(lambda: False)
        found = False
        for jndex in range(index-preamble,index):
            number = int(numbers[jndex])
            if obj[number]:
                found = True
                break
            obj[sumTo-number] = True
        
        if found is False:
            break
    return sumTo

invalidNumber = xmasSearch(numbers)
print(invalidNumber)


def inchWorm(numbers,sumTo):
    start = 0
    worm = 0
    body = []
    for i,number in enumerate(numbers):
        worm += int(number)
        body.append(int(number))
        while worm > sumTo:
            worm -= int(numbers[start])
            start += 1
            body.pop(0)

        if worm == sumTo:
            break
    

    return min(body) + max(body)


print(inchWorm(numbers,invalidNumber))