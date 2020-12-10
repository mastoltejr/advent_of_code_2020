import re

x = 'cid:315 iyr:2012 hgt:192cm eyr:2023 pid:873355140 byr:1925 hcl:#cb2c03'
g = dict(re.findall(r"([a-z]+):(\S+)",x,re.IGNORECASE))

fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}

with open('day4.txt','r') as f:
    rows = f.read().split('\n\n')
    obj = dict({})
    valid = 0
    for row in rows:
        if len(row) == 0:
            keys = set(obj.keys())
            if fields.issubset(keys):
                print('Valid: {}/{}'.format(valid+1,len(rows)))
                valid += 1
            else:
                print('Invalid missing fields:' + str(fields-keys))
            obj = dict({})
            print('=====')
        else:
            obj = {**obj,**dict(re.findall(r"([a-z]+):(\S+)",row,re.IGNORECASE))}

print(valid)


#### part2

import re
valid = 0

def valid_byr(byr):
    return int(byr) >= 1920 and int(byr) <= 2002

def valid_iyr(iyr):
    return int(iyr) >= 2010 and int(iyr) <= 2020

def valid_eyr(eyr):
    return int(eyr) >= 2020 and int(eyr) <= 2030

def valid_hgt(hgt):
    try:
        (num,unit) = re.match(r"(\d+)(in|cm)",hgt,re.IGNORECASE).groups()
        return (unit == 'in' and (int(num) >= 59 and int(num) <= 76)) or (unit == 'cm' and (int(num) >= 150 and int(num) <= 193))
    except AttributeError:
        return False

def valid_hcl(hcl):
    return re.search(r"#[\da-z]{6}",hcl,re.IGNORECASE) is not None

def valid_ecl(ecl):
    return ecl in ['amb','blu','brn','gry','grn','hzl','oth']

def valid_pid(pid):
    return re.search(r"[\d]{9}",pid,re.IGNORECASE) is not None

def valid_passport(obj):
    fields = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
    ret = {}
    if not valid_byr(obj.get('byr',0)):
        ret['byr'] = obj.get('byr')
    if not valid_iyr(obj.get('iyr',0)):
        ret['iyr'] = obj.get('iyr')
    if not valid_eyr(obj.get('eyr',0)):
        ret['eyr'] = obj.get('eyr')
    if not valid_hgt(obj.get('hgt','fail')):
        ret['hgt'] = obj.get('hgt')
    if not valid_hcl(obj.get('hcl','fail')):
        ret['hcl'] = obj.get('hcl')
    if not valid_ecl(obj.get('ecl','fail')):
        ret['ecl'] = obj.get('ecl')
    if not valid_pid(obj.get('pid','fail')):
        ret['pid'] = obj.get('pid')
    
    print(ret)
    return len(ret) == 0

with open('day4.txt','r') as f:
    rows = f.read().split('\n\n')
    for (i,row) in enumerate(rows):
        row = row.replace('\n',' ')
        obj = dict(re.findall(r"([a-z]+):(\S+)",row,re.IGNORECASE))
        if valid_passport(obj):
            valid += 1
        else:
            print('Item ' + str(i))
            print('=================')
print(valid)