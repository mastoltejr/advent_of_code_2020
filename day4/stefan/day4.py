from functools import reduce, partial
import re

req_keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def add_field(fields, raw_field):
    key, val = raw_field.split(":")
    fields[key] = val
    return fields


def read_passport(raw_pass):
    return reduce(add_field, raw_pass.split(), {})


def read_all_passports(content):
    raw_passports = content.split('\n\n')
    passports = map(read_passport, raw_passports)
    return passports


def contains_keys(passport):
    return req_keys.issubset(set(passport.keys()))


def valid_years(passport):
    return passport['byr'].isnumeric() \
        and passport['iyr'].isnumeric() \
        and passport['eyr'].isnumeric() \
        and 1920 <= int(passport['byr']) <= 2002 \
        and 2010 <= int(passport['iyr']) <= 2020 \
        and 2020 <= int(passport['eyr']) <= 2030


def valid_height(passport):
    matches = re.match(r"(\d+)(in|cm)", passport['hgt'])
    if not matches:
        return False
    height, units = matches.groups()
    if units == 'cm':
        return 150 <= int(height) <= 193
    return 59 <= int(height) <= 76

    
def valid_hair(passport):
    return re.search(r"#[\d\w]{6}", passport['hcl'])


def valid_eyes(passport):
    return passport['ecl'] in eye_colors


def valid_pid(passport):
    return re.search(r"^\d{9}$", passport['pid'])

def validate_passport(passport):
    return contains_keys(passport) \
        and valid_years(passport) \
        and valid_height(passport) \
        and valid_hair(passport) \
        and valid_eyes(passport) \
        and valid_pid(passport)


with open("day4_in","r") as f:
    raw_passports = f.read().split('\n\n')
    passports = map(read_passport, raw_passports)
    first_pass = list(filter(contains_keys, passports))
    second_pass = list(filter(validate_passport, first_pass))
    print("p1: ", len(first_pass))
    print("p2: ", len(second_pass))
    